from fastapi import FastAPI

app = FastAPI(
    title="Knowledge Hub API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Knowledge Hub API"
    }