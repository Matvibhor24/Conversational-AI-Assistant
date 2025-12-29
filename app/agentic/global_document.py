from app.documents.chunker import chunk_text
from app.documents.summarize_chunk import summarize_chunk
from app.documents.summarize_final import synthesize_summary
from app.documents.store import update_document
from app.documents.session import DocumentSession


def generate_global_summary(document: DocumentSession) -> str:
    """
    Generate and store a global summary lazily.
    Called ONLY for global scope document intent.
    """
    if document.has_summary:
        return document.summary

    chunks = chunk_text(document.raw_text)
    chunk_summaries = []
    for chunk in chunks:
        chunk_summaries.append(summarize_chunk(chunk))

    final_summary = synthesize_summary(chunk_summaries)
    document.summary = final_summary
    document.has_summary = True
    update_document(document)

    return final_summary
