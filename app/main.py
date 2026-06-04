from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.auth import router as auth_router

app = FastAPI(
    title="Knowledge Hub API",
    version="1.0.0"
)

app.include_router(
    health_router,
    prefix="/api"
)

app.include_router(
    auth_router,
    prefix="/api"
)

@app.get("/")
def root():
    return {
        "message": "Knowledge Hub API"
    }