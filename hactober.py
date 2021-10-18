
#use Chrome webdriver 94 and your github creds
import time
import re
import os.path
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import smtplib

#Selenium automation
driver = webdriver.Chrome(service_log_path='NUL')
url = "https://hacktoberfest.digitalocean.com/profile"
#Just give your github username and password 
CREDS = {'user':'YOUR USERNAME','pass':'YOUR PASSWORD'}

driver.get(url)
print("URL WORKING")
time.sleep(5)

driver.find_element_by_xpath("//*[@id='container']/div/div/div[4]/a[1]").click()
time.sleep(5)
print("GITHUB LOGIN")

#username
username = driver.find_element_by_xpath("//*[@id='login_field']")
driver.get
username.click()
username.send_keys(CREDS['user'])
time.sleep(3)

#password
password = driver.find_element_by_xpath("//*[@id='password']")
password.click()
password.send_keys(CREDS['pass'])
time.sleep(3)

#login
driver.find_element_by_xpath("//*[@id='login']/div[3]/form/div/input[12]").click()
time.sleep(3)
print("GITHUB LOGGED SUCCESSFULLY")

#web scarping starts

progress=[]
contribution=[]
time.sleep(10)

page = requests.get(url)
print(page)
soup = bs(page.text,'lxml')
#for tag in soup.find_all(class_='block text-xl').findAll('span'):
prog = driver.find_element_by_xpath("//*[@id='container']/div[2]/section[1]/div[4]/span[1]")
print(prog.text)
time.sleep(2)

comp = driver.find_element_by_xpath("//*[@id='container']/div[2]/section[1]/div[3]/span[1]")
print(comp.text)

#IT will works for my table of data on contribution
#Change as per your contribution for checking matures or excluded project data
# #Extracting table data
c1 = driver.find_element_by_xpath("//*[@id='container']/div[2]/section[2]/div/table[1]/tbody/tr/td[3]")
c2 = driver.find_element_by_xpath("//*[@id='container']/div[2]/section[2]/div/table[6]/tbody/tr/td[3]")
c3 = driver.find_element_by_xpath("//*[@id='container']/div[2]/section[2]/div/table[9]/tbody/tr/td[3]")
c4 = driver.find_element_by_xpath("//*[@id='ontainer']/div[2]/section[2]/div/table[11]/tbody/tr/td[3]")


print(c1.text)
print(c2.text)
print(c3.text)
print(c4.text)

#Mailing or SMS services need to be added where it will check the data every 15 min and update 
