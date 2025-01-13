PATH_RAW_DATASET_HUGGINGFACE = "JulianVelandia/unal-repository-dataset"
DATASET_OUTPUT_FILE = "finetuning_dataset.json"
DATASET_OUTPUT_FILE_TEST = "finetuning_dataset_test.json"
DATASET_OUTPUT_FILE_TRAIN = "finetuning_dataset_train.json"
OUTPUT_DATASET_HUGGINGFACE = "unal-repository-dataset-instruct"
OUTPUT_DATASET_HUGGINGFACE_TEST = "unal-repository-dataset-test-instruct"
OUTPUT_DATASET_HUGGINGFACE_TRAIN = "unal-repository-dataset-train-instruct"
HUGGINGFACE_TOKEN = ":)"
USER_HUGGING_FACE = "JulianVelandia"
MAX_RETRIES_LLM = 3

PROMPT_TEMPLATE = (
    "Formule una pregunta relevante sobre el siguiente fragmento (En la pregunta debe ir toda la "
    "información para entender la pregunta, agrega contexto a la pregunta si es necesario) y responda de forma breve. "
    "(Responde en el formato, sin texto adicional)"
    "Formato: PREGUNTA: [pregunta aquí] RESPUESTA: [respuesta aquí]. Fragmento: '{fragmento}'"
)
