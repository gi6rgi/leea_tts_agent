from typing import Type

from elevenlabs.client import ElevenLabs
from leea_agent_sdk.agent import Agent

from app.models import Input, Output
from app.settings import settings
from app.tts_service import TTSService

# TODO: Move this from global variables. Dependencies should be initialized and injected at application startup.
tts_client = ElevenLabs(api_key=settings.eleven_labs_api_key)
tts_service = TTSService(client=tts_client)


class TTSAgent(Agent):
    name: str = settings.app_name
    description: str = settings.app_description
    input_schema: Type[Input] = Input
    output_schema: Type[Output] = Output

    async def run(self, request_id: str, input_: Input) -> Output:
        # await self.push_log(request_id=request_id, message=f"Received request_id: {request_id}")

        # TODO: ask about bytes streaming.
        audio_bytes = b""
        async for chunk in tts_service.text_to_speech(text=input_.text):
            audio_bytes += chunk

        # await self.push_log(request_id=request_id, message=f"request_id: {request_id} has been processed")
        return Output(audio_bytes=audio_bytes)
