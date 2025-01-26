from fastapi import FastAPI
from app.api.endpoints import router as api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Replace with specific origins if needed.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Include the API router
app.include_router(api_router)
