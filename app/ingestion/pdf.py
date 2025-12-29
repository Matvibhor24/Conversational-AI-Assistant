import fitz  # PyMuPDF
from docling.document_converter import DocumentConverter
from app.ingestion.models import IngestedDocument


def extract_pdf(path: str) -> IngestedDocument:
    doc = fitz.open(path)
    text = "".join(page.get_text() for page in doc).strip()

    if len(text) > 500:
        return IngestedDocument(
            raw_text=text, source_type="pdf", extraction_method="pymupdf"
        )

    converter = DocumentConverter()
    result = converter.convert(path)
    text = result.document.export_to_text()

    return IngestedDocument(
        raw_text=text, source_type="pdf", extraction_method="docling"
    )
