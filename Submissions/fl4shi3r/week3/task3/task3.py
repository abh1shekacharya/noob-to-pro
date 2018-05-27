from bs4 import BeautifulSoup
from urllib.request import urlopen
import re,pprint
req_page = urlopen("https://jsonplaceholder.typicode.com/comments").read()
soup = BeautifulSoup( req_page ,'lxml')
text= str(soup.string)
unique=re.compile(r'[a-zA-Z0-9._%+-]+@+[a-zA-Z0-9.-]+\.+[a-zA-Z]{2,6}')
email_list = unique.findall(text)
dictn= {}
for email in email_list:
    dictn.setdefault(email, 0)
    dictn[email] = dictn[email] + 1
for i in dictn :
	if dictn[i]==1:
		print(i)
