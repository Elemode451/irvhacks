from fastapi import APIRouter, HTTPException
from app.services.openai_service import get_names_from_openai
from app.services.zembra_service import query_zembra
from app.services.cms_service import query_general_dataset
from app.utils.helpers import clean_name
from app.utils.helpers import split_name


from pydantic import BaseModel
import logging 
from app.utils.constants import RESULT


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Define the router
router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Welcome to the API! Use /query to interact."}

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
        # names = get_names_from_openai(request.query)
        names = ["skibidi"]
        
        if names == []:
            return {"result": "Kelly Bach"}
        # Step 2: Query Zembra for each name
        print("We move onto the next phase")
        zembra_responses = RESULT
        
        print("now that we have a zembra response, WE MOBILIZE!")
        names = []
        for doctor_entry in zembra_responses["result"]:
            for doctor_name in doctor_entry:
                names.append(doctor_name)

        new_names = list(map(lambda name: split_name(clean_name(name)), names))
        print(new_names)

        # Step 3: Open CMS query
        print(query_general_dataset(names))
    



        return {"result": zembra_responses}

    except Exception as e:
        print(e)
        # raise HTTPException(status_code=418, detail=str(e))



