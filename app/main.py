from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.auth import router as auth_router
from app.api.collections import router as collections_router
from app.api.resources import router as resources_router

app = FastAPI(
    title="Knowledge Hub API",
    version="1.0.0",
    swagger_ui_parameters={"persistAuthorization": True}
)

@app.get("/")
def root():
    return {
        "message": "Knowledge Hub API"
    }

app.include_router(
    health_router,
    prefix="/api"
)

app.include_router(
    auth_router,
    prefix="/api"
)

app.include_router(
    collections_router,
    prefix="/api"
)

app.include_router(
    resources_router,
    prefix="/api"
)