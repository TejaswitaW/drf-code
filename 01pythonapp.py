import requests
URL = "http://127.0.0.1:8000/student/1"

r = requests.get(url=URL) # response

print("r: ",r)

data = r.json()

print(data)

print(type(data))