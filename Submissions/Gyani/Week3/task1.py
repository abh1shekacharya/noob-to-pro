import requests
url='http://www.mocky.io/v2/5b026eb43000007a00cee110'
r=requests.get(url)
flag=r.headers['flag']

print("The flag is :",flag)

print("The rest all headers are :-")
for name, value in r.headers.items():
	print(name,' ', value)
