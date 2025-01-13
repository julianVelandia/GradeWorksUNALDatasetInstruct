from openai import OpenAI

from GradeWorksUNALDatasetInstruct.utils.dataset_loader import load_remote_dataset
from constants import DATASET_OUTPUT_FILE, MAX_RETRIES, PROMPT_TEMPLATE, OUTPUT_DATASET_HUGGINGFACE, HUGGINGFACE_TOKEN, \
    USER_HUGGING_FACE, PATH_RAW_DATASET_HUGGINGFACE
from services.openai_service import generate_prompt_completion
from utils.file_handler import load_existing_data, save_entry, upload_dataset_to_huggingface
from utils.text_processor import clean_raw_content, split_content_into_chunks


def process_and_save(data):
    processed_data = load_existing_data(DATASET_OUTPUT_FILE)
    processed_fragments = {item["fragment"] for item in processed_data}
    raw_data = data[-1]

    for _, value in raw_data.items():

        clean_content = clean_raw_content(value)
        chunks = split_content_into_chunks(clean_content)

        for chunk in chunks:
            if chunk in processed_fragments:
                continue
            result = generate_prompt_completion(client, chunk, PROMPT_TEMPLATE, MAX_RETRIES)
            if result:
                save_entry(DATASET_OUTPUT_FILE, result)
                processed_fragments.add(chunk)


def run():
    #dataset = load_remote_dataset(PATH_RAW_DATASET_HUGGINGFACE)
    #data = [row for row in dataset]
    #process_and_save(data)
    upload_dataset_to_huggingface(
        output_file=DATASET_OUTPUT_FILE,
        repo_name=OUTPUT_DATASET_HUGGINGFACE,
        token=HUGGINGFACE_TOKEN,
        org=USER_HUGGING_FACE,
    )


client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
if __name__ == "__main__":
    run()
