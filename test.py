import requests

API_KEY = "Z8KCqm6iY3tD3NBvkJHSFwjMuo9ongcl"

url = "https://api.deepinfra.com/v1/inference/meta-llama/Meta-Llama-3-8B-Instruct"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "input": "What is DeepInfra?"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
