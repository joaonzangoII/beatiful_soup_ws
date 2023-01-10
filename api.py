import requests

headers = {
    "Accept", "application/vnd.proxypay.v2+json"
    "Content-Type", "application/json"
    "Authorization", "Token " + "reh8inj33o3algd2tpi6tkcnrqf8rjj2"; }
result = requests.get("https://api.github.com/users/joaonzangoii" , headers=headers)
print(result.json()["login"])