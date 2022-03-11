import requests

# Remember this BASE_URL or IP is our localhost not container`s IP.
# BASE_URL = "http://127.0.0.1:5000/"
# BASE_URL = "http://localhost:5000/"
BASE_URL = "http://192.168.0.101:5000/"


####### GET #######
response = requests.get(BASE_URL + "")
print(response.json())
