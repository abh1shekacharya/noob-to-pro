import requests

r = requests.get('http://www.mocky.io/v2/5b026eb43000007a00cee110')
headers = r.headers
flag = headers['Flag']
print('The flag is : ' + flag)

print('\nHere are all Headers')
for key in headers:
    print(key + ' --> ' + headers[key])
