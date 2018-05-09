#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import datetime
import time
from getpwd import getpwd

driver = webdriver.Firefox()
'''http://gate.jd.com/InitCart.aspx?pid=4993737&pcount=1&ptype=1'''

def login():
    driver.get("https://passport.jd.com/new/login.aspx")
    time.sleep(3)
    driver.find_element_by_link_text("账户登录").click()
    print("Enter your user name:")
    username=input()
    driver.find_element_by_name("loginname").send_keys(username)
    password=getpwd("Enter your password:\n")
    driver.find_element_by_name("nloginpwd").send_keys(password)
    print("\n请输入验证码后回车，如无需输验证码请直接回车")
    verification=input()
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(3)
    driver.get("https://cart.jd.com/cart.action")
    time.sleep(3)
    driver.find_element_by_link_text("去结算").click()
    now = datetime.datetime.now()
    #now_time = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    print('登录成功，可继续操作!')

def buy_on_time(buytime):
    print("设定时间："+buytime)
    print("等待中....")
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            driver.find_element_by_id('order-submit').click()
            time.sleep(3)
            print(now.strftime('%Y-%m-%d %H:%M:%S'))
            print('purchase success')
        time.sleep(0.5)

login()
buy_on_time('2018-08-27 10:00:00')
