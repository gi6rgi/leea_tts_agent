from pydantic import BaseModel


class Input(BaseModel):
    text: str


class Output(BaseModel):
    audio_bytes: bytes
