from ollama import chat

def ask_llm(prompt):
    response = chat(
        model="qwen3:14b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.message.content