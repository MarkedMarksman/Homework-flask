import requests

response = requests.post(url='http://127.0.0.1:5000/ads',json={
    'title': 'Hello World',
    'description': 'Selling the world again',
    'user_name': 'A Man who sold the world'})
print(response.status_code)
print(response.text)