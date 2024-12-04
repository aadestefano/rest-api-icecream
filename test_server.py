import requests

print(requests.get("http://127.0.0.1:8000/flavors/0").json())
print(requests.get("http://127.0.0.1:8000/flavors?flavorName=Chocolate").json())

print("Adding an item:")
response = requests.post(
        "http://127.0.0.1:8000/flavors",
        json = {"flavorName": "Strawberry", "description": "Berry flavor!", "price": 1.50, "count": 100, "id": 4}
)
print(response.json())


print(requests.get("http://127.0.0.1:8000/").json())

