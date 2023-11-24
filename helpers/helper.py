import configparser, requests, json
from config import API_KEY

apple_KEY = API_KEY

# gets top article of macrumors.com
def execute_apple():
    requestUrl = f'https://newsapi.org/v2/everything?domains=macrumors.com&apiKey={API_KEY}'
    requestHeaders = {
    'Accept': 'application/json'
    }
    
    response = requests.get(requestUrl, headers=requestHeaders)
    
    # convert to json format
    response_dict = json.loads(response.text)
    return response_dict["articles"][0]["url"]


# gets top article of techcrunch.com
def execute_techcrunch():
    requestUrl = f'https://newsapi.org/v2/everything?domains=techcrunch.com&apiKey={API_KEY}'
    requestHeaders = {
    'Accept': 'application/json'
    }

    response = requests.get(requestUrl, headers=requestHeaders)

    # convert to json format
    response_dict = json.loads(response.text)
    return response_dict["articles"][0]["url"]

