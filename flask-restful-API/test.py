import requests
# run app.py file first, then run this file

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"likes": "10", "name": "how to make tea", "views": "100"},
#     {"likes": "20", "name": "how to make biryani", "views": "200"},
#     {"likes": "30", "name": "how to make mass gainer", "views": "300"},
# ]

#### update data ######
# response = requests.patch(BASE + "video/1", {"likes": 10, "name": "how to make something"})
# print(response.json())

#### delete ######
# response = requests.delete(BASE + "video/1")
# print(response)

#### get data ######
response = requests.get(BASE + "video/1")
print(response.json())


# print("inserting...")
# response = requests.put(BASE + f"video/4", {"likes": "40", "name": "how to make protien", "views": "400"})
# print(response.json())

# for item in range(len(data)):
#     response = requests.put(BASE + f"video/{item}", data[item])

    # this response is nothing but returned values from methods in our created Resource

# input()
# print("fetching data...")
# response = requests.get(BASE + "video/10")
# print("fetched data: ", response.json())



#
# input()
# print("fetching data...")
# response = requests.get(BASE + "video/0")
# print("fetched data: ", response.json())
#
# input()
# print("deleting data...")
# response = requests.delete(BASE + f"video/0")
# print(response)
#
#
# input()
# print("fetching data...")
# response = requests.get(BASE + "video/1")
# print("fetched data: ", response.json())



