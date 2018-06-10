import requests
r = requests.get('http://www.mocky.io/v2/5b026eb43000007a00cee110')
for x in r.headers:
  print (x + ":" + r.headers[x])
