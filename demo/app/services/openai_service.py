from openai import OpenAI
import os
from config.settings import settings

n = 6
client = OpenAI(api_key=settings.openai_api_key)

# Constants for OpenAI system prompts
SEARCH_INFO = (
    "You are to embody the role of a MEDICAL search engine. "
    "You will only provide names in response to the query that is asked, with no other additional information. "
)

DOCTOR_NAME = (
    "If you are provided with a singular name, or asked for information on a DOCTOR'S name, just output the exact name back."
)

NUM_NAMES = (
    f"You will provide a list of up to {n} names. JUST names. Separate each one with the character |. Make sure it's a full name, and no weird artifacts are included. Include all medical prefixes, like Dr, or MD."
)

def get_names_from_openai(query: str) -> list[str]:
    print("we are good")
    """
    Use OpenAI to get a list of names based on the query.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SEARCH_INFO},
            {"role": "system", "content": DOCTOR_NAME},
            {"role": "system", "content": NUM_NAMES},
            {"role": "user", "content": query},
        ],
        temperature=0.4,
    )

    print("we are not good")

    names_result = response.choices[0].message

    if(names_result.content.__contains__("|")):
        return [name.strip() for name in names_result.content.split("|") if name.strip()]
    else:
        return []
