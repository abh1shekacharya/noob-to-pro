import requests
import json
import csv

r = requests.get('https://jsonplaceholder.typicode.com/posts')

data = json.loads(r.text)

csv_file = open('scrap4.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['userId', 'id', 'title', 'body'])

num = 10
for i in data:
    for key in data:
        csv_writer.writerow([key['userId'], key['id'], key['title'], key['body']])
