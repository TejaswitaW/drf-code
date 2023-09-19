import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    # if id=None, return all data
   
    json_data = json.dumps(data)

    headers = {'content-Type':'application/json'}

    r = requests.get(url=URL,headers=headers,data=json_data)

    print("Get Request: ",requests.get(url=URL,headers=headers,data=json_data))
    
    data = r.json()

    print(data)

get_data(16)

def post_data():
    data = {
        'name':'Ramji',
        'roll':80,
        'city':'Pune'
    }

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)

    r = requests.post(url=URL,headers=headers,data=json_data)

    data = r.json()

    print(data)

#post_data()

def update_data():
    data = {
        'id':14,
        'name':'KT',
        'city':'Bengaluru'
    }

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)

    r = requests.put(url=URL,headers=headers,data=json_data)

    data = r.json()

    print(data)

#update_data()

def delete_data():
    data = {
        'id':7,
    }

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)

    r = requests.delete(url=URL,headers=headers,data=json_data)

    data = r.json()

    print(data)

#delete_data()

