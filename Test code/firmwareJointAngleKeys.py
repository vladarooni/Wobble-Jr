import requests
import json

ip = "192.168.4.1"   #only works when roarm is in AP mode

response = requests.get(f"http://{ip}/js?json={{\"T\":105}}")
print("Raw feedback JSON: ", response.text)

# parse and print keys
angles = json.loads(response.text)
print("Keys in feedback: ", angles.keys())

#Raw feedback JSON:  {"T":1051,"x":157.5373094,"y":-268.4068236,"z":233.2414975,"b":-1.040038974,"s":0.004601942,"e":1.578466231,"t":3.144660615,"torB":-28,"torS":28,"torE":32,"torH":20}
#Keys in feedback:  dict_keys(['T', 'x', 'y', 'z', 'b', 's', 'e', 't', 'torB', 'torS', 'torE', 'torH'])