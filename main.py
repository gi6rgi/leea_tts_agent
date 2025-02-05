from leea_agent_sdk import runtime

from app.logs import logger
from app.settings import settings
from app.tts_agent import TTSAgent


def main():
    runtime.start(agent=TTSAgent(), wallet_path=settings.wallet_path)
    logger.info("Application startup completed")


if __name__ == "__main__":
    main()
