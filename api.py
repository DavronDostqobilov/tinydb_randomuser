import requests

base_url = "https://randomuser.me/api/"

def data(n):
    param={
        'X-Api-Key':'7b3b6035a5c94aee8908aaa68c9a6fe4',
        'results':n
    }
    r=requests.get(base_url,params=param)
    data=r.json()
    return data['results']

#print(data(5))