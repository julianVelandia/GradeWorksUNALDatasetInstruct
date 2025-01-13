import json
import os
import random


def split_dataset(dataset_path, train_path, test_path, split_ratio=0.75):
    if not os.path.exists(dataset_path):
        print(f"El archivo {dataset_path} no existe.")
        return

    with open(dataset_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    random.seed(42)
    random.shuffle(data)

    split_index = int(len(data) * split_ratio)

    train_data = data[:split_index]
    test_data = data[split_index:]

    with open(train_path, "w", encoding="utf-8") as train_file:
        json.dump(train_data, train_file, ensure_ascii=False, indent=4)

    with open(test_path, "w", encoding="utf-8") as test_file:
        json.dump(test_data, test_file, ensure_ascii=False, indent=4)
