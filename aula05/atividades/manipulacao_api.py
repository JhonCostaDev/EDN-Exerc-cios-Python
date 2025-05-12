import requests

url = 'https://randomuser.me/api/'


def get_data(url:str) -> dict:
    try:
        response = requests.get(url)

        if response.status_code != 200:
            raise requests.exceptions.HTTPError(response.status_code)
        
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.HTTPError, requests.exceptions.InvalidURL) as e:
        print(e)
    else:    
        data = response.json()
        return data
        
data = get_data(url)

user_dict = data['results'][0]

for key, value in user_dict.items():
    if len(value) > 1:
        print(f'{key}: {value}')


