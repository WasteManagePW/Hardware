import http.client
import json

connection = http.client.HTTPConnection('localhost', 8000, timeout=10)
connection.request("GET", "/")
response = connection.getresponse()

print("Status: {} and reason: {}".format(response.status, response.reason))

headers = {'Content-type': 'application/json'}
foo = {'text': 'Hello HTTP'}
json_data = json.dumps(foo)

connection.request('POST', '/post', json_data, headers)
response = connection.getresponse()
print(response.read().decode())