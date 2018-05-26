import requests
import json

r = requests.get('https://jsonplaceholder.typicode.com/comments')
emails = []

data = json.loads(r.text)

for i in data:
    for key in data:
        emails.append(key['email'])

print(set(emails))