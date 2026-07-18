# core/logger.py

import logging
import os


os.makedirs("logs", exist_ok=True)


logger = logging.getLogger("agent-engine")
logger.setLevel(logging.INFO)


file_handler = logging.FileHandler(
    "logs/engine.log",
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)