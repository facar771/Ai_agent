from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass(frozen=True)
class Settings:
    # API
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))

    # OpenAI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    MODEL: str = os.getenv("MODEL", "gpt-4o-mini")

    # Budget
    DRY_RUN: bool = os.getenv("DRY_RUN", "true").lower() == "true"
    MAX_BUDGET: float = float(os.getenv("MAX_BUDGET", "4.50"))

    # Paths
    DATA_DIR: str = "data"
    UPLOAD_DIR: str = "data/uploads"
    SPEND_LOG: str = "data/spend_log.json"


settings = Settings()