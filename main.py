from leea_agent_sdk import runtime

from app.logs import logger
from app.tts_agent import TTSAgent


def main():
    runtime.start(agent=TTSAgent())
    logger.info("Application startup completed")


if __name__ == "__main__":
    main()
