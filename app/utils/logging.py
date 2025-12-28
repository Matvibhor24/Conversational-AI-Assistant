import logging
import json
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(message)s")

logger = logging.getLogger("assistant")


def log_event(event: str, data: dict, request_id: str | None = None):
    """
    Logs a structured event.
    """
    payload = {"timestamp": datetime.utcnow().isoformat(), "event": event, **data}
    if request_id:
        payload["request_id"] = request_id
    logger.info(json.dumps(payload))
