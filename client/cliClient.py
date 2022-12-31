import requests
import json

url = "http://127.0.0.1:5000"


while True:
    sentence = input("You : ")
    r = requests.post(url+'/assistant',data = json.dumps({"msg":sentence}))
    r = json.loads(r.text)
    print(r["msg"])