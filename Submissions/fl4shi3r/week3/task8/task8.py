from selenium import webdriver
from getpass import getpass
import time
username = input("Enter your username(Should be greater than 6 letters: ")
password = getpass('Enter your password')
chrome = webdriver.Chrome('/root/Downloads/chromedriver')
chrome.get('http://www.babblenow.com')

uname = chrome.find_element_by_id('login-username')
uname.send_keys(username)

passwd = chrome.find_element_by_id('login-password')
passwd.send_keys(password)

submit = chrome.find_element_by_xpath("//button[@class='btn btn-primary btn-block']")
submit.click()
for i in range(20):
	c_id = random.randrange(42000000,80000000)
	comment = chrome.find_element_by_id(c_id+'_textarea')
	comment.send_keys("Python is great , 'noob-to-pro'") 
	comment_submit = chrome.find_element_by_xpath("//a[@class='btn btn-danger btn-sm add-comment-button']")
	comment_submit.click()
