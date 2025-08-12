import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    WABA_TOKEN = os.getenv("WABA_TOKEN", "")
    WABA_PHONE_ID = os.getenv("WABA_PHONE_ID", "")
    WABA_API_VERSION = os.getenv("WABA_API_VERSION", "")
    VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "cambiar")

    GOOGLE_CREDENTIAS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "./service_account.json")
    GSHEET_ID = os.getenv("GSHEET_ID", "")

    TIMEZONE = os.getenv("TIMEZONE", "America/Bogota")
    MAX_FILE_MB = int(os.getenv("MAX_FILE_MB", "10"))
    BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

    ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "")

    UPLOAD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "uploads"))
    LOG_DIR = os.path-abspath(os.path.join(os.path.dirname(__file__), "..", "logs"))

settings = Settings()

