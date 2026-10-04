from embedding import create_embedding
from vector_db import collection


def search_documents(query, top_k=3):

    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results["documents"][0]
    ids = results["ids"][0]

    sources = []

    for chunk_id in ids:

        filename = chunk_id.rsplit("_chunk_", 1)[0]

        sources.append(filename)

    return documents, sources