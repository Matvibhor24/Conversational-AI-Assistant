from typing import Dict
from app.documents.session import DocumentSession

_DOCUMENTS: Dict[str, DocumentSession] = {}


def create_document(document_id: str, raw_text: str) -> DocumentSession:
    doc = DocumentSession(document_id=document_id, raw_text=raw_text)
    _DOCUMENTS[document_id] = doc
    return _DOCUMENTS[document_id]


def get_document(document_id: str) -> DocumentSession:
    return _DOCUMENTS[document_id]


def update_document(document: DocumentSession):
    _DOCUMENTS[document.document_id] = document
