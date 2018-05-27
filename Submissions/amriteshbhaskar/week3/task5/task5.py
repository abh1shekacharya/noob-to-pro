import requests
from bs4 import BeautifulSoup

s = requests.session()
signUp = s.get('http://www.babblenow.com')

values = {
    'username' : input('Enter Username: '),
    'password': input('Enter Password: '),
    'email': input('Enter Email Id(not required): ')
}

result = s.post(
    'http://www.babblenow.com/helpers/index/signup_newuser.php',
    data = values
)

result = s.get('http://www.babblenow.com')

soup = BeautifulSoup(result.text, 'lxml')

if (soup.find('form').div.input['class'][0] == 'sign_user'):
    print('UserName Exists or Password length is less than 6')
else:
    print('Registration Successful')

