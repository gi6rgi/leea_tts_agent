from elevenlabs.client import ElevenLabs

from app.logs import logger


class TTSService:
    def __init__(self, client: ElevenLabs):
        self._client = client

    async def text_to_speech(self, text: str, voice_id: str = "JBFqnCBsd6RMkjVDRZzb"):
        logger.info(
            f"Received text-to-speech request. Text: '{text}' with voice ID: '{voice_id}'"
        )
        audio_stream = self._client.text_to_speech.convert_as_stream(
            text=text, voice_id=voice_id
        )
        for chunk in audio_stream:
            if isinstance(chunk, bytes):
                yield chunk
