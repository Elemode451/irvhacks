from fastapi import FastAPI
import os
from dotenv import load_dotenv
from app.api.endpoints import router as api_router

app = FastAPI()

# Include the API router

app.include_router(api_router)
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ZEMBRA_API_KEY = os.getenv("ZEMBRA_API_KEY")
