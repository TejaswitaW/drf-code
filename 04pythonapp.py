import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    # if id=None, return all data
    json_data = json.dumps(data)
    r = requests.get(url=URL,data=json_data)
    print("Get Request: ",requests.get(url=URL,data=json_data))
    data = r.json()
    print(data)

get_data()

def post_data():
    data = {
        'name':'Kush T',
        'roll':110,
        'city':'Bengaluru'
    }

    json_data = json.dumps(data)

    r = requests.post(url=URL,data=json_data)

    data = r.json()

    print(data)

#post_data()

def update_data():
    data = {
        'id':4,
        'name':'Luv T',
        'roll':111,
        'city':'Indor City'
    }

    json_data = json.dumps(data)

    r = requests.put(url=URL,data=json_data)

    data = r.json()

    print(data)

#update_data()

def delete_data():
    data = {
        'id':1,
    }

    json_data = json.dumps(data)

    r = requests.delete(url=URL,data=json_data)
    # print("r: ",r)
    data = r.json()

    print(data)

#delete_data()