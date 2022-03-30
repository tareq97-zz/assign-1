import os
import requests

os.environ['NO_PROXY'] = '127.0.0.1'
r = requests.get("http://127.0.0.1:5000")
r.json()
