# import Flask
import requests
# from temp.py import tempreading

URL = "http://localhost:3000"

# location given here 
message = "hello from python server"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'data':message} 
  
# sending get request and saving the response as response object 
r = requests.post(url = URL, data = PARAMS) 
  
# extracting data in json format 
data = r.text

print(data)
