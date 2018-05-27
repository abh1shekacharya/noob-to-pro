from bs4 import BeautifulSoup
from urllib.request import urlopen
req_page = urlopen("https://jsonplaceholder.typicode.com/posts").read()
soup = BeautifulSoup( req_page ,'lxml')
text= str(soup.string)
task_file = open('/root/Pictures/noob-to-pro/Submissions/fl4shi3r/week3/task2/task2.csv','a')
task_file.write('userId,id,title,body\n')
task_file.close()
ch=''
for i in range(len(text)):
    if text[i]==':':
        j=i
        while(text[j]!=','):
            if text[j+1]=='}':
                 ch=ch+''
            else:
                ch=ch+text[j+1]
            j=j+1
            if text[j]=='}':
                ch=ch+""
                break
task_file = open('/root/Pictures/noob-to-pro/Submissions/fl4shi3r/week3/task2/task2.csv','a+')
task_file.write(ch)
task_file.close()
        
        
