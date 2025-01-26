from fastapi import APIRouter, HTTPException
from app.services.openai_service import get_names_from_openai
from app.services.zembra_service import query_zembra
from app.services.cms_service import query_general_dataset
from app.utils.helpers import clean_name
from app.utils.helpers import split_name
from app.utils.helpers import filter_json

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
        # Step 1: Get names from GPT
        names = get_names_from_openai(request.query)
        print("\n\n\n\n")
        print(names)
        print("\n\n\n\n")
        if names == []:
            return {"result": "No names Bach"}
        
        print("We move onto the next phase")
        zembra_responses = query_zembra(names)
        print("\n\n\nnow that we have a zembra response, WE MOBILIZE!")

        
        names = []
        """
        for doctor_info in zembra_responses:
            print(doctor_info)
            for check_errors in doctor_info.values():
                if 'error' not in check_errors.keys():
                    for info in doctor_info:
                        names.append(doctor_info)

        """
        clean_zembra = []
        for doctor_info in zembra_responses:
            print(doctor_info)
            for check_errors in doctor_info.values():
                if 'error' not in check_errors.keys():
                    for name in doctor_info.keys():
                        names.append(name)
                    for info in doctor_info:
                        clean_zembra.append(doctor_info)

        
        filtered_all_doctors = [filter_json(doctor) for doctor in clean_zembra]
                       
   


        # clean_names = list(map(lambda name: split_name(clean_name(name)), names))
        print("\n\n\n\n")
        print(clean_zembra)

        # # Step 3: CMS query (spreadsheet)
        # cms_results = []
        # for name_pair in clean_names:
        #     (first_name, last_name) = name_pair
        #     cms_results.append(query_general_dataset(first_name, last_name))
            
        # print(cms_results)

    
        return {"result": zembra_responses}

    except Exception as e:
        print(e)
        # raise HTTPException(status_code=418, detail=str(e))



