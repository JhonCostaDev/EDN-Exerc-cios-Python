import requests

url = 'https://github.com/JhonCostaDev/EDN-Exerc-cios-Python/blob/main/main.py'

response = requests.get(url)

print(response.status_code)