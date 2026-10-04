import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="research_documents"
)


def add_documents(chunks, embeddings, filenames):

    ids = []

    for i, filename in enumerate(filenames):
        ids.append(f"{filename}_chunk_{i}")

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    print(f"✅ Added {len(chunks)} chunks to ChromaDB")