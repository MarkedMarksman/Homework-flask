import requests
#POST
response = requests.post(url='http://127.0.0.1:5000/ads',json={
    'title': 'Hello World',
    'description': 'Selling the world again',
    'user_name': 'A Man who sold the world'})
print(response.status_code)
print(response.text)

# GET
response = requests.get('http://127.0.0.1:5000/ads/7')

print(response.status_code)
print(response.text)

# DELETE
response = requests.delete('http://127.0.0.1:5000/ads/5')

print(response.status_code)
print(response.text)