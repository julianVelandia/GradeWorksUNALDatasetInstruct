DATASET_INPUT_FILE = "dataset.json"
DATASET_OUTPUT_FILE = "data/finetuning_dataset.json"
MAX_RETRIES = 3

PROMPT_TEMPLATE = (
    "Formule una pregunta relevante sobre el siguiente fragmento (En la pregunta debe ir toda la "
    "información para entender la pregunta, agrega contexto a la pregunta si es necesario) y responda de forma breve. "
    "(Responde en el formato, sin texto adicional)"
    "Formato: PREGUNTA: [pregunta aquí] RESPUESTA: [respuesta aquí]. Fragmento: '{fragmento}'"
)