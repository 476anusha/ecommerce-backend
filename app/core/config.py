from dotenv import load_dotenv
import os


load_dotenv()

class Settings:
    MONGO_URI: str = os.getenv("MONGO_URI")
    DB_NAME: str = os.getenv("DB_NAME")

settings = Settings()
