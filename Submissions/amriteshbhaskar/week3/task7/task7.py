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
    print('\nRegistration Successful\n\n')

result = s.get('http://www.babblenow.com/gettingtoknowbabblenow')
soup = BeautifulSoup(result.text, 'lxml')

ans = input('which network do you want to join:\n 1) University/school\n 2) Explore Networks\n ')

if ans == '1' :
    network = input('Enter the Network Name(like IIIT Allahabad, BITS Pilani')
    answer = input('What is the answer of asked question')     # couldn't find the way to get the question (under Process)
    values = {
        'network': network,
        'answer': answer
    }
    s.post(
        'http://www.babblenow.com/helpers/explorenetworks/submit_answer_and_join_network.php',
        data= values
    )
else:
    network = input('Enter the Network Name(like funny, memes)')
    values = {
        'network': network,
    }
    s.post(
        'http://www.babblenow.com/helpers/explorenetworks/submit_answer_and_join_network.php',
        data= values
    )

name = input('Enter the virtual Name')
bio = input('Enter the Bio')
values = {
    'virtualname': name,
    'bio': bio
}
s.post(
    'http://www.babblenow.com/helpers/home/submit_virtualname.php',
    data= values
)

