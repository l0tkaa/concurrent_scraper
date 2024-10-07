import requests
from logger import log_request, log_response, log_error

def fetch_data_from_api(endpoint, params=None):
    try:
        log_request(endpoint)
        response = requests.get(endpoint, params=params)
        log_response(endpoint, response.status_code)

        if response.status_code == 200:
            return response.json()
        else:
            log_error(endpoint, f'Status code: {response.status_code}')
            return None
    except Exception as e:
        log_error(endpoint, str(e))
        return None
