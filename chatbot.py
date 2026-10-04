from ollama import chat
from config import MODEL_NAME
from memory import messages


def ask_ai(question):
    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    response = chat(
        model=MODEL_NAME,
        messages=messages
    )

    answer = response["message"]["content"]

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    return answer