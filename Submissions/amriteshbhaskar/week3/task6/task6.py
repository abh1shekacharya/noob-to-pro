from bs4 import BeautifulSoup
import requests

s = requests.session()
url = s.get('http://www.babblenow.com')

values = {
    'username': input('Enter the Username: '),
    'password': input('Enter the Password: ')
}

result = s.post(
    'http://www.babblenow.com/helpers/index/authenticate_user.php',
    data= values
)

result = s.get('http://www.babblenow.com')

soup = BeautifulSoup(result.text, 'lxml')

try:
    if soup.find('div').ul or soup.find('span', class_='title').text:
        print('Logged in Successfully')
except:
    print('Incorrect Username or Password')