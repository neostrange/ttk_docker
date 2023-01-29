import requests


dct = "20081010"
text = "He will leave the town before his wife reaches there"

data = {"input":text, "dct": dct}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


response = requests.post("http://localhost:5050/annotate", json=data, headers=headers)

# print(response.content)
print(response.text)
