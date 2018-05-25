import urllib.request
res = urllib.request.urlopen('http://www.mocky.io/v2/5b026eb43000007a00cee110')
print("Flag is ",res.getheader('Flag'))
print(res.getheaders())
