import os
from typing import List

class Settings:
    @property
    def ALLOWED_ORIGINS(self) -> List[str]:
        return os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")

    @property
    def API_KEY(self) -> str:
        return os.getenv("API_KEY", "airq-production-key-45892")

    @property
    def DEFAULT_PLAN(self) -> str:
        return os.getenv("DEFAULT_PLAN", "free")

    @property
    def JWT_SECRET(self) -> str:
        return os.getenv("JWT_SECRET", "SuperStrongSecretKey_928374928374")

    @property
    def JWT_EXPIRES_MIN(self) -> int:
        return int(os.getenv("JWT_EXPIRES_MIN", "120"))

    @property
    def COOKIE_DOMAIN(self) -> str:
        return os.getenv("COOKIE_DOMAIN", "your-backend-name.onrender.com")

settings = Settings()
