import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env file


class Settings:
    port: int = int(os.getenv("PORT", 8003))
    database_url: str = os.getenv("DATABASE_URL")
    jwt_secret: str = os.getenv("JWT_SECRET")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM")


settings = Settings()
