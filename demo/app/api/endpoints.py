from fastapi import APIRouter, HTTPException
from app.services.openai_service import get_names_from_openai
from app.services.zembra_service import query_zembra
from pydantic import BaseModel

# Define the router
router = APIRouter()

# Pydantic model for request validation
class QueryRequest(BaseModel):
    query: str

@router.post("/query")
async def query(request: QueryRequest):
    """
    Endpoint to handle user queries. 
    Uses OpenAI to get names and queries Zembra for details.
    """
    if not request.query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    try:
        # Step 1: Use OpenAI to get a list of names
        names = get_names_from_openai(request.query)

        # Step 2: Query Zembra for each name
        zembra_responses = query_zembra(names)

        return {"result": zembra_responses}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
