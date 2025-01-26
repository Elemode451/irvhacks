from pydantic import BaseModel
from typing import Dict

class DoctorDetails(BaseModel):
    specialty: str
    location: str


class FetchResponse(BaseModel):
    result: Dict[str, DoctorDetails]