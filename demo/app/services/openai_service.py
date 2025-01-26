import openai
import os

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Constants for OpenAI system prompts
SEARCH_INFO = (
    "You are to embody the role of a MEDICAL search engine. "
    "You will only provide names in response to the query that is asked, with no other additional information. "
    "You will provide a list of up to 15 names. JUST names. Separate each one with the character |. Make sure it's a full name, and no weird artifacts are included."
)

DOCTOR_NAME = (
    "If you are provided with a singular name, or asked for information on a DOCTOR'S name, just output the exact name back."
)

def get_names_from_openai(query: str) -> list[str]:
    """
    Use OpenAI to get a list of names based on the query.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SEARCH_INFO},
            {"role": "system", "content": DOCTOR_NAME},
            {"role": "user", "content": query},
        ],
        temperature=0.4,
    )

    names_result = response["choices"][0]["message"]["content"]
    return [name.strip() for name in names_result.split("|") if name.strip()]
