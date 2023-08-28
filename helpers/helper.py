import configparser, requests, json


# Method to read config file settings
# this code also taken from url: https://www.codeproject.com/Articles/5319621/Configuration-Files-in-Python
def read_config():
    config = configparser.ConfigParser()
    config.read('configurations.ini')
    return config

# defining secret api key
config = read_config()
API_KEY = config["FTPSettings"]["newsapi_key"]

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

