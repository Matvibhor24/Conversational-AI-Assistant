from docling.document_converter import DocumentConverter
from app.ingestion.models import IngestedDocument


def extract_with_docling(path: str, source_type: str) -> IngestedDocument:
    converter = DocumentConverter()
    result = converter.convert(path)

    text = result.document.export_to_text()

    return IngestedDocument(
        raw_text=text, source_type=source_type, extraction_method="docling"
    )
