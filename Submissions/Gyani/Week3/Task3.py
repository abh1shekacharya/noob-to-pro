import requests
import re
from bs4 import BeautifulSoup


url='https://jsonplaceholder.typicode.com/comments'

r=requests.get(url)
s=BeautifulSoup(r.text,'lxml')
s=s.find('p').text
num=1
print("Unique emails are : -")
for line in re.findall(r"\{\n.*\n.*\n.*\n.*\n",s):
	l=line.replace('\n',',').replace(': ',',').split(',')
	s2=l[11].replace('"','')
	print(num," ",s2)
	num=num+1
