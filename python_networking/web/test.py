#!/usr/bin/python3
import requests

user = {'id': "odhiambohumphrey78@gmail.com", 'password': '48maran88'}
v = requests.get("https://intranet.alxswe.com/projects/263")

print(v.text)
