import re
import requests
from bs4 import BeautifulSoup

url='https://jsonplaceholder.typicode.com/posts'
r=requests.get(url)
s=BeautifulSoup(r.text,'lxml')
content=s.find('p').text

with open ('document.csv','w') as w:
	w.write("UserId,Id,Title,Body\n")

	for line in re.findall(r"\{\n.*\n.*\n.*\n.*\n",content):
		l=line.replace('\n',',').replace(': ',',').split(',')
		s1=l[8].replace('"','')
		s2=l[11].replace('"','')
		res=l[2]+','+l[5]+','+s1+','+s2
		w.write(res)
		w.write("\n")
print("The extracted contents are saved in the file document.csv")		
