import configparser, requests, json

config = read_config()
API_KEY = config["FTPSettings"]["api_key"]

# Method to read config file settings
# this code also taken from url: https://www.codeproject.com/Articles/5319621/Configuration-Files-in-Python
def read_config():
    config = configparser.ConfigParser()
    config.read('configurations.ini')
    return config

# defining secret api key
config = read_config()
API_KEY = config["FTPSettings"]["api_key"]

# to easily generate an api call response
#  - may not need actually, might be more cumbersome!
def execute_nyt():
    requestUrl = 'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={API_KEY}'
    requestHeaders = {
    'Accept': 'application/json'
    }
    
    response = requests.get(requestUrl, headers=requestHeaders)
    
    # convert to json format
    response_dict = json.loads(response.text)
    return response_dict["results"][0]["url"]


    #############
# TODO: write bloomberg function...
# def execute_bloom():
  #  requestUrl = ''
  ##############


  # TODO: write a third function, or
  # better yet, a more dynamic function 
  # which involves some web scraping????

