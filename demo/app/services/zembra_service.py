import requests
from urllib.parse import quote
from config.settings import settings  

BASE_URL = "https://api.zembra.io/listing/"

def get_URI(name: str) -> str:
    """
    Construct the complete API URI for querying a doctor by name.
    """
    return f"{BASE_URL}find?name={quote(name)}&networks[]=healthgrades"

def query_zembra(names: list[str]) -> list[dict]:
    """
    Search a list of names using the Zembra API and return the results.

    Args:
        names (list[str]): List of doctor names to query.

    Returns:
        list[dict]: A list of responses from the Zembra API, one for each name.
    """
    if not names:
        return []

    print("Starting the Zembra queries...")
    zembra_responses = []

    headers = {
        "Authorization": f"Bearer {settings.zembra_api_key}",
        "Accept": "application/json",
    }

    for name in names:
        print(f"Processing name: {name}")
        try:
            url = get_URI(name)
            print(f"Requesting URL: {url}")

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                print(f"Success for {name}: {response.json()}")
                zembra_responses.append({name: response.json()})
            else:
                print(f"Failed for {name} with status {response.status_code}")
                zembra_responses.append({
                    name: {"error": f"Failed with status {response.status_code}"}
                })
        except Exception as e:
            print(f"Error for {name}: {str(e)}")
            zembra_responses.append({
                name: {"error": f"Exception occurred: {str(e)}"}
            })

    return zembra_responses
