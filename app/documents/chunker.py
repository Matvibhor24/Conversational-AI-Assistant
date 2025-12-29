def chunk_text(text: str, max_chars: int = 4000) -> list[str]:
    """
    Split text into chunks of approx max_chars.
    """
    chunks = []
    start = 0

    while start < len(text):
        end = start + max_chars
        chunks.append(text[start:end])
        start = end
    return chunks
