import requests
import time
import json
from temp import get_enviromentals

URL = "http://192.168.178.27:3000/temp"

payload = get_enviromentals()
  
while True:
    requests.post(url = URL, json = payload)
    time.sleep(5)
