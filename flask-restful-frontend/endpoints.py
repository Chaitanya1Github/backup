import requests

BASE_URL = "http://127.0.0.1:5000/"

####### GET #######
response = requests.get(BASE_URL + "book/book1")
print(response.json())

####### PUT #######
response = requests.put(BASE_URL + "book/", {"book_name": "see me", "author_name": "me"})
print(response.json())


