import requests

# Requires internet access. This example calls a public test API.
response = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
response.raise_for_status()
print("Status code:", response.status_code)
print("Response JSON:", response.json())
