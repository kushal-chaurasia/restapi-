import requests
import json

URL = "http://127.0.0.1:8000/cardcreate"

data = {
    'name': 'tseting',
    'card_no': 8527419630456123,
    'expiry' : '2014-01-01',
    'cvv' : 852   
}
json_data = json.dumps(data)
r = requests.post(url = URL , data = json_data)
data = r.json()
print(data)