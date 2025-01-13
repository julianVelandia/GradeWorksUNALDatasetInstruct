import json
import os
from collections import Counter


def eda(output_file):
    if not os.path.exists(output_file):
        print(f"El archivo {output_file} no existe.")
        return

    with open(output_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    total_records = len(data)
    print(f"Total de registros: {total_records}")

    avg_prompt_length = sum(len(entry["prompt"]) for entry in data) / total_records
    avg_completion_length = sum(len(entry["completion"]) for entry in data) / total_records
    print(f"Longitud promedio del prompt: {avg_prompt_length:.2f} caracteres")
    print(f"Longitud promedio del completion: {avg_completion_length:.2f} caracteres")

    word_counts = Counter(word for entry in data for word in entry["prompt"].split())
    most_common_words = word_counts.most_common(5)
    print("Palabras más frecuentes en los prompts:")
    for word, count in most_common_words:
        print(f"  {word}: {count}")

    print("\nEjemplos representativos:")
    print("Primer registro:")
    print(f"  Prompt: {data[0]['prompt']}")
    print(f"  Completion: {data[0]['completion']}\n")
    print("Último registro:")
    print(f"  Prompt: {data[-1]['prompt']}")
    print(f"  Completion: {data[-1]['completion']}\n")

    longest_fragment = max(data, key=lambda x: len(x["fragment"]))
    shortest_fragment = min(data, key=lambda x: len(x["fragment"]))
    print("Fragmento más largo:")
    print(f"  {longest_fragment['fragment'][:100]}... ({len(longest_fragment['fragment'])} caracteres)")
    print("Fragmento más corto:")
    print(f"  {shortest_fragment['fragment'][:100]}... ({len(shortest_fragment['fragment'])} caracteres)")
