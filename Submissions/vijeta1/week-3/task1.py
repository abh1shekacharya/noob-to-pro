import requests

flag=requests.get('http://www.mocky.io/v2/5b026eb43000007a00cee110')

for i in flag.headers:
	print(i+":"+flag.headers[i])
