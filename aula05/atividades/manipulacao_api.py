import requests

url = 'https://randomuser.me/api/'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print('erro')

print(type(data['results'][0]))
user = data['results'][0]

print(user.get('name').get('first'))

