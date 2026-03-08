import uvicorn
from fastapi import FastAPI

from app.config.settings import settings
import app.models  # noqa: F401 - register all models for SQLAlchemy relationship resolution
from app.routes.health import router as health_router
from app.routes.auth import router as auth_router

app = FastAPI()

app.include_router(health_router)
app.include_router(auth_router, prefix="/users")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0",
                port=settings.port, reload=True)
