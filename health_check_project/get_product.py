import requests
import json

response = requests.get('https://fakestoreapi.com/products/1')

if response.status_code == 200:
    data = response.json()
    print(f"Product: {data['title']}")
    print(f"Price: ${data['price']}")    
else:
    print(f"Caught Error: status code {response.status_code}")