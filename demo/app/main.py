from fastapi import FastAPI

from app.api.endpoints import router as api_router

app = FastAPI()

# Include the API router

app.include_router(api_router)