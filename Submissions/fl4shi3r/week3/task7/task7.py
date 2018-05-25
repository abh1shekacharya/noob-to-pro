from selenium import webdriver
from getpass import getpass
import time
username = input("Enter your username(Should be greater than 6 letters: ")
password = getpass('Enter your password')
chrome = webdriver.Chrome('/root/Downloads/chromedriver')
chrome.get('http://www.babblenow.com')
element = chrome.find_element_by_xpath("//span[@class='btn btn-default signupBtn center-block']")
element.click()

time.sleep(3)
uname = chrome.find_element_by_id('signup-username')
uname.send_keys(username)

passwd = chrome.find_element_by_id('signup-password')
passwd.send_keys(password)

submit = chrome.find_element_by_xpath("//button[@class='btn btn-info btn-block signup_submit']")
submit.click()
time.sleep(3)
tos = chrome.find_element_by_xpath("//input[@class='tos_check']")
tos.click()
done = chrome.find_element_by_xpath("//button[@class='btn btn-info btn-block tos_submit']")
done.click()
print("Kindly do recaptcha and leave")
time.sleep(15)
contn = chrome.find_element_by_xpath("//button[@class='btn btn-info btn-block captcha_submit']")
contn.click()
iiita = chrome.find_element_by_xpath("//a[@class='initial-network private-1']")
print("Where do Btech students have their regular classes?")
ans = input()
answer = chrome.find_element_by_xpath("//input[@class='answer-join-network']")
answer.send_keys(ans)
network = chrome.find_element_by_xpath("button[@class='btn btn-primary']")
network.click()

