import requests

url = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

r = requests.get(url, headers=headers)

print("Status:", r.status_code)
print(r.text[:500])
