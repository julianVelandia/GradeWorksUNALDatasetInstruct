PATH_RAW_DATASET_HUGGINGFACE = "JulianVelandia/unal-repository-dataset"
DATASET_OUTPUT_FILE = "finetuning_dataset.json"
OUTPUT_DATASET_HUGGINGFACE = "unal-repository-dataset-instruct"
HUGGINGFACE_TOKEN = ":)"
USER_HUGGING_FACE = "JulianVelandia"
MAX_RETRIES = 3

PROMPT_TEMPLATE = (
    "Formule una pregunta relevante sobre el siguiente fragmento (En la pregunta debe ir toda la "
    "información para entender la pregunta, agrega contexto a la pregunta si es necesario) y responda de forma breve. "
    "(Responde en el formato, sin texto adicional)"
    "Formato: PREGUNTA: [pregunta aquí] RESPUESTA: [respuesta aquí]. Fragmento: '{fragmento}'"
)
