import requests
import json

def auth_api(url):
	token_auth = '81f1be1f922a337e70f66cbe94269c20f34117a7'

	headers={'Authorization': 'Token ' + token_auth}
	response = requests.get(url, headers=headers)
	return response

url_1 = "http://localhost:8000/api/v1/?format=json"
url_2 = "http://localhost:8000/api/insee/?format=json&search={}".format("Camiers")

response1 = auth_api(url_1)
response2 = auth_api(url_2)

print(response1.json())
print(response2.json())
