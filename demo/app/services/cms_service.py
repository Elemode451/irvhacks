import requests

BASE_URL = "https://openpaymentsdata.cms.gov/resource/fb3a65aa-c901-4a38-a813-b04b00dfa2a9.json"

def query_general_dataset(first_name, last_name):
    """
    Query the General Dataset to retrieve payment details for a specific physician.
    """

    params = {
        "physician_first_name": first_name,
        "physician_last_name": last_name
    }

    try:
        response = requests.get(BASE_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            print(f"Results for {first_name} {last_name}:")
            return data
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return None

physician_data = query_general_dataset("John", "Doe")
print(physician_data)
