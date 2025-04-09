
import requests

url = "https://api.tfl.gov.uk/Line/Mode/tube/Status"

def fetch_data():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
