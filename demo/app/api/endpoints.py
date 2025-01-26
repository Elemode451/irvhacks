from fastapi import APIRouter, HTTPException

from app.services.zembra_service import fetch_zembra_data

router = APIRouter()

@router.get("/fetch")
async def fetch_data(name: str, network: str = "healthgrades"):

    try:
        data = fetch_zembra_data(name, network)

        return {"result": data}

    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))