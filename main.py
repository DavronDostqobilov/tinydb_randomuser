from tinydb import TinyDB
import api
data=api.data
db = TinyDB('data.json', intent=4)
doc={
    "first_name": f"{data['name']['first']}",
    "last_name": f"{data['name']['last']}",
    "age": data['dob']['age'],
    "phone": f"{data['phone']}",
    "country": f"{data['location']['country']}",
    "email": f"{data['email']}",
}
db.insert(doc)