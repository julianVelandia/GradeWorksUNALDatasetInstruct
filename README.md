# Grade Works UNAL Dataset Instruct

Dataset of the Grade Works of the UNAL repository in format Question : Answer.
It is required to raise an [LMstudio](https://lmstudio.ai/) server

Link repository: https://repositorio.unal.edu.co/handle/unal/5

Dataset kaggle: https://www.kaggle.com/datasets/juliancamilovelandia/gradeworksunaldatasetinstruct

Dataset HuggingFace: https://huggingface.co/datasets/JulianVelandia/unal-repository-dataset-instruct

This dataset is a { question : answer } version of the dataset of the degree works of the Universidad Nacional de Colombia, Ideal for fine tuning work on language models

# Format dataset
```json
[
  {
    "prompt": "¿Cómo se determina la vida útil del proyecto básico y complejo de iluminación en un hospital según la norma ISO 15686?",
    "completion": "Se determina multiplicando el valor en años de la tabla 1 por factores de estimación de vida útil de la tabla 2, dependiendo de las condiciones de la edificación.",
    "fragment": "implementados sistemas ..."
  }
]
```
The transform process is as follows

![image](https://github.com/user-attachments/assets/a2ebc554-ed15-48f0-a171-ba20147800e2)

**Main Statistics**:
- Total records: **16,700**.
- Average prompt length: **142.98 characters**.
- Average completion length: **148.80 characters**.
- Most frequent words in prompts:  
  - **de**: 26,715  
  - **la**: 18,616  
  - **en**: 17,742  
  - **el**: 16,711  
  - **y**: 10,559  
