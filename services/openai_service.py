def generate_prompt_completion(client, chunk, prompt_template, max_retries=3, model="model-identifier"):
    completion_prompt = prompt_template.format(fragmento=chunk)

    for attempt in range(1, max_retries + 1):
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": completion_prompt}],
            temperature=0.2
        )
        response = completion.choices[0].message.content.strip().replace("'", "")

        if response.startswith("PREGUNTA:") and "RESPUESTA:" in response:
            question_part = response.split("PREGUNTA:")[1].split("RESPUESTA:")[0].strip()
            answer_part = response.split("RESPUESTA:")[1].strip()
            return {"prompt": question_part, "completion": answer_part, "fragment": chunk}

        print(f"Reintento {attempt}/{max_retries}, fragmento: {chunk}")

    print(f"Error fragmento: {chunk}")
    return None
