import requests
import os

# Zembra API Key
ZEMBRA_API_KEY = os.getenv("ZEMBRA_API_KEY")
ZEMBRA_URI = "https://api.zembra.io/listing/find?name="

def query_zembra(names: list[str]) -> list[dict]:
    """
    Search a list of names using the Zembra API and return the results.
    """
    if not names:
        return []

    zembra_responses = []
    headers = {
        "Authorization": f"Bearer {ZEMBRA_API_KEY}",
        "Accept": "application/json",
    }

    for name in names:
        try:
            url = f"{ZEMBRA_URI}{name}"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                zembra_responses.append({name: response.json()})
            else:
                zembra_responses.append({name: {"error": f"Failed to fetch data with status {response.status_code}"}})
        except Exception as e:
            zembra_responses.append({name: {"error": str(e)}})

    return zembra_responses
