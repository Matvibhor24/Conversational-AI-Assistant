import whisper
from app.ingestion.models import IngestedDocument

_model = whisper.load_model("base")


def transcribe_audio(path: str) -> IngestedDocument:
    result = _model.transcribe(path)

    return IngestedDocument(
        raw_text=result["text"], source_type="audio", extraction_method="whisper"
    )
