from pydantic import BaseModel

class WhatsAppMessage(BaseModel):
    object: str | None = None

    