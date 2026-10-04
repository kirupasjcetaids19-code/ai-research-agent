from pathlib import Path
from pypdf import PdfReader


DOCUMENTS_FOLDER = Path("documents")


def load_pdfs():
    documents = []

    for pdf_file in DOCUMENTS_FOLDER.glob("*.pdf"):
        reader = PdfReader(pdf_file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        documents.append({
            "filename": pdf_file.name,
            "text": text
        })

    return documents


if __name__ == "__main__":
    documents = load_pdfs()

    print(f"Found {len(documents)} PDF files\n")

    for document in documents:
        print("=" * 60)
        print(f"FILE: {document['filename']}")
        print(f"Characters: {len(document['text'])}")
        print("=" * 60)