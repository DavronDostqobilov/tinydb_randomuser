from tinydb import TinyDB
import requests
import api

db = TinyDB('data.json', indent=4)
url=api.base_url
def data(n):
    param={
        'X-Api-Key':'7b3b6035a5c94aee8908aaa68c9a6fe4',
        'results':n
    }
    r=requests.get(url,params=param)
    data=r.json()
    return data['results']

data=data(50)


for i in range(len(data)):
    doc={
        "first_name": f"{data[i]['name']['first']}",
        "last_name": f"{data[i]['name']['last']}",
        "age": data[i]['dob']['age'],
        "phone": f"{data[i]['phone']}",
        "country": f"{data[i]['location']['country']}",
        "email": f"{data[i]['email']}",
    }
    db.insert(doc)
