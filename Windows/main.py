from selenium import webdriver
import time
import random
import os 
import sys

path = '/Driver/chromedriver.exe'

email = str(input("Type in your Insta E-mail/Username"))
password = str(input("Type in your Insta Password"))
dmuser = str(input("Type The Username you want to spam:- "))
n = int(input("Type the number of times you want to spam-: "))
spam = str(input('Type What you want to spam: '))

driver = webdriver.Chrome(path)

def spammg(element):
    
    element = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(random.choice(spam))

    element = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
    


def searchdm(element):
    element = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]').click()
    
    time.sleep(2)
    
    element = driver.find_element_by_xpath(
        '/html/body/div[4]/div/div[2]/div[1]/div/div[2]/input').send_keys(dmuser)
    
    time.sleep(2)
    
    element = driver.find_element_by_xpath(
        '/html/body/div[4]/div/div[2]/div[2]/div[1]/div/div[3]/button/span').click()
    
    time.sleep(2)
    
    element = driver.find_element_by_xpath(
        '/html/body/div[4]/div/div[1]/div/div[2]/div/button').click()
    
    time.sleep(3)
    
    for i in range(n):
        spammg(element)


driver.get('https://instagram.com')

time.sleep(3)

element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(email)

element = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)

time.sleep(3)

element = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()

time.sleep(3)

element = driver.find_element_by_xpath(
    '/html/body/div[4]/div/div/div[3]/button[2]').click()

time.sleep(3)

element = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()

time.sleep(3)

searchdm(element)
