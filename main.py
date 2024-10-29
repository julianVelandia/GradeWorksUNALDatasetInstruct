from openai import OpenAI
import re
import json
import os

DATASET_INPUT_FILE = "dataset.json"
DATASET_OUTPUT_FILE = "dataset_finetuning.json"
MAX_RETRIES = 3

PROMPT_TEMPLATE = (
    "Formule una pregunta relevante sobre el siguiente fragmento (En la pregunta debe ir toda la "
    "información para entender la pregunta, agrega contexto a la pregunta si es necesario) y responda de forma breve. "
    "(Responde en el formato, sin texto adicional)"
    "Formato: PREGUNTA: [pregunta aquí] RESPUESTA: [respuesta aquí]. Fragmento: '{fragmento}'"
)

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


def clean_raw_content(raw_content):
    """Limpia el contenido, elimina caracteres especiales y recorta las primeras 5000 y las últimas 12000 palabras."""
    cleaned_content = re.sub(r'[-\n]+', ' ', raw_content).strip()
    words = cleaned_content.split()
    trimmed_content = words[5000:len(words) - 12000] if len(words) > 17000 else words[5000:]
    return ' '.join(trimmed_content)


def split_content_into_chunks(content, n=150):
    """Divide el contenido en fragmentos de n palabras cada uno."""
    words = content.split()
    return [' '.join(words[i:i + n]) for i in range(0, len(words), n)]


def generate_prompt_completion(chunk, model="model-identifier"):
    """Genera el prompt, obtiene la completion y verifica el formato."""
    completion_prompt = PROMPT_TEMPLATE.format(fragmento=chunk)

    for attempt in range(1, MAX_RETRIES + 1):
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": completion_prompt}],
            temperature=0.2
        )
        response = completion.choices[0].message.content.strip()

        if response.startswith("PREGUNTA:") and "RESPUESTA:" in response:
            question_part = response.split("PREGUNTA:")[1].split("RESPUESTA:")[0].strip()
            answer_part = response.split("RESPUESTA:")[1].strip()
            return {"prompt": question_part, "completion": answer_part, "fragment": chunk}

        print(f"Reintento {attempt}/{MAX_RETRIES} fallido para el fragmento: {chunk}")

    print(f"Formato incorrecto después de {MAX_RETRIES} intentos para el fragmento: {chunk}")
    return None


def load_existing_data():
    """Carga el dataset de salida si ya existe y contiene datos, y lo devuelve como lista."""
    if os.path.exists(DATASET_OUTPUT_FILE):
        with open(DATASET_OUTPUT_FILE, "r", encoding="utf-8") as file:
            print(file)
            data = []
            for line in file:
                while not line.endswith('}'):
                    line = line[:-1]
                print('line', line)

                if line.strip():
                    print('type', type(line))

                    data.append(json.loads(line))
            print(3)
            return data
    return []


def save_entry(entry):
    """Guarda un nuevo registro en el archivo de salida, cada uno en una línea separada."""
    with open(DATASET_OUTPUT_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(entry, ensure_ascii=False) + ", \n")
    print(f"Entrada guardada: {entry}")


def process_and_save(data):
    """Procesa cada registro del dataset y guarda el resultado incrementalmente."""
    processed_data = load_existing_data()
    processed_fragments = {item["fragment"] for item in processed_data}
    i = 0

    for entry in data.values():
        if "raw_content" in entry:
            clean_content = clean_raw_content(entry["raw_content"])
            chunks = split_content_into_chunks(clean_content)

            for chunk in chunks:
                i += 1
                if any(fragment in chunk or chunk in fragment for fragment in processed_fragments):
                    print(f'Chunk ya procesado, {i}')
                    continue



                result = generate_prompt_completion(chunk)
                if result:
                    save_entry(result)
                    processed_fragments.add(chunk)
                    print(f"Procesado y guardado: {result}")
                else:
                    print(f"Saltando fragmento por errores de formato: {chunk}")


def run():
    """Entry point: carga el dataset y procesa los datos de forma incremental."""
    with open(DATASET_INPUT_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    process_and_save(data)


run()