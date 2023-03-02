from tinydb import TinyDB
from api import data

db = TinyDB('data.json', indent=4)

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
