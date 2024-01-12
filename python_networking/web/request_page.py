#!/usr/bin/python3
import requests

r = requests.get("https://davidmmasters.com/wp-content/uploads/2017/05/how-to-keep-from-getting-so-pissed-off.jpg")

with open("comic.png", "wb") as f:
    f.write(r.content)

payload = {'email': 'odhiambohumphrey78@gmail.com', 'password': '48maran88'}

session = requests.Session()


v = requests.post("https://intranet.alxswe.com/auth/sign_in", data=payload)

if v.status_code == 200:
    print("Login successful")
else:
    print("Login failed")
