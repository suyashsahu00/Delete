import requests

response = requests.post(
    'http://127.0.0.1:5000/books/',
    json={'title': 'My Book'}
)

print(response.json())
