from search_db import search_documents
from chatbot import ask_ai


def ask_pdf(question):

    chunks, ids = search_documents(question, top_k=3)

    context = "\n\n".join(chunks)

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not present in the context, say:
"I could not find the answer in the document."

Context:
{context}

Question:
{question}

Give a clear and simple answer.
"""

    answer = ask_ai(prompt)

    return answer, ids