import tempfile
from app.documents.store import create_document
from app.ingestion.pdf import extract_pdf
from app.ingestion.docling_extractor import extract_with_docling
from app.ingestion.audio import transcribe_audio
import uuid


def ingest_file(file) -> str:
    suffix = file.filename.split(".")[-1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as tmp:
        tmp.write(file.file.read())
        path = tmp.name

    if suffix == "pdf":
        ingested = extract_pdf(path)
    elif suffix in {"docx", "png", "jpg", "jpeg"}:
        ingested = extract_with_docling(path, source_type=suffix)
    elif suffix in {"mp3", "wav", "m4a"}:
        ingested = transcribe_audio(path)
    else:
        raise ValueError("Unsupported file type")

    document_id = str(uuid.uuid4())
    create_document(document_id=document_id, raw_text=ingested.raw_text)

    return document_id
