import requests

base_url = "https://randomuser.me/api/"
r=requests.get(base_url)
data=r.json()
data=data['results'][0]
#print(data[0]['name']['first'])