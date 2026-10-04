from pdf_reader import load_pdfs
from chunker import chunk_text
from embedding import create_embedding
from vector_db import add_documents


def index_pdfs():

    documents = load_pdfs()

    all_chunks = []
    all_embeddings = []
    all_filenames = []

    for document in documents:

        filename = document["filename"]
        text = document["text"]

        print("\n" + "=" * 60)
        print(f"📄 Processing: {filename}")
        print("=" * 60)

        chunks = chunk_text(text)

        print(f"Total chunks: {len(chunks)}")

        for chunk in chunks:

            embedding = create_embedding(chunk)

            all_chunks.append(chunk)
            all_embeddings.append(embedding)
            all_filenames.append(filename)

    add_documents(
        all_chunks,
        all_embeddings,
        all_filenames
    )

    print("\n" + "=" * 60)
    print(f"✅ Total chunks indexed: {len(all_chunks)}")
    print("✅ All PDFs indexed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    index_pdfs()