# config.py
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.environ.get("MODEL_DIR", os.path.join(BASE_DIR, "models"))
USE_GPT4 = os.environ.get("USE_GPT4", "false").lower() == "true"
MAX_PROCESS_SECONDS = 28  # leave margin below 30s
