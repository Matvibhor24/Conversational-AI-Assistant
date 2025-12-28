from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="General AI Assistant")

app.include_router(router)
