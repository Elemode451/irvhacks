import requests

ZEMBRA_API_URL = "https://api.zembra.io/listing/find"

ZEMBRA_AUTH_TOKEN = "your_bearer_token"


def fetch_zembra_data(name: str, network: str):

    params = {"name": name, "networks[]": network}

    headers = {

        "Authorization": f"Bearer {ZEMBRA_AUTH_TOKEN}",

        "Accept": "application/json",

    }

    response = requests.get(ZEMBRA_API_URL, params=params, headers=headers)

    if response.status_code != 200:

        raise Exception(f"Zembra API error: {response.text}")

    return process_data(response.json())


def process_data(data):

    processed = {}

    for item in data.get("data", []):

        doctor_name = item.get("name")

        processed[doctor_name] = {

            "specialty": item.get("specialty"),

            "location": item.get("location"),

        }

    return processed