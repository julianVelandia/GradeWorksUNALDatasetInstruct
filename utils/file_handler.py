import json
import os

from huggingface_hub import HfApi

from GradeWorksUNALDatasetInstruct.constants import DATASET_OUTPUT_FILE


def upload_dataset_to_huggingface(output_file, repo_name, token, org=None):
    api = HfApi()
    repo_id = f"{org}/{repo_name}" if org else repo_name

    try:
        api.create_repo(repo_id=repo_id, token=token, repo_type="dataset", exist_ok=True)
        print(f"Repositorio {repo_id} creado o ya existente.")
    except Exception as e:
        print(f"Error al crear el repositorio: {e}")
        return

    try:
        api.upload_file(
            path_or_fileobj=output_file,
            path_in_repo=DATASET_OUTPUT_FILE,
            repo_id=repo_id,
            repo_type="dataset",
            token=token
        )
        print(f"Archivo subido exitosamente al repositorio {repo_id}.")
    except Exception as e:
        print(f"Error al subir el archivo: {e}")


def load_existing_data(output_file):
    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                print(f"Error al cargar el archivo JSON existente: {e}")
    return []


def save_entry(output_file, entry):
    data = []

    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                print(f"Error al cargar el archivo JSON existente: {e}")

    data.append(entry)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
