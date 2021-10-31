# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import sys
import datetime
import settings

def main():

    username = settings.USERNAME
    print('target account: ' + username)
    # driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

    # ログインページに遷移する
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

    # 2秒スリープ（待機）
    time.sleep(2)

    # ユーザ名、パスワードを入力してログイン
    id = browser.find_element_by_name("username")
    id.send_keys(username)
    password = browser.find_element_by_name("password")
    password.send_keys(settings.PASSWORD)
    password.send_keys(Keys.RETURN)

    # 3秒スリープ（待機）
    time.sleep(3)

    # 対象アカウントのInstagramページにアクセス
    browser.get('https://www.instagram.com/' + username + '/')

    # 3秒スリープ（待機）
    time.sleep(3)

    # 画面上で、フォロワーのリンクをクリック
    follower_button = browser.find_elements_by_css_selector("li.Y8-fY")[1]
    follower_button.click()

    # 3秒スリープ（待機）
    time.sleep(3)


    # フォロワーの一覧は、ポップアップウインドウで表示されます
    dialog = browser.find_element_by_css_selector("div.isgrP")
    for i in range(200):
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
        time.sleep(random.randint(500,1000)/1000)

    page_url = browser.page_source
    soup = BeautifulSoup(page_url,"lxml")
    elements = soup.find_all("a", {"class": "FPmhX notranslate _0imsa"})
    followers = []
    # 取得できたフォロワー名を配列にadd
    for value in elements:
        followers.append(value.text)

    # csvに書き出し
    df= pd.Series(followers)

    # 現在時刻の取得
    now = datetime.datetime.now()
    df.to_csv('csv/' + username + '_follower_list_' + now.strftime('%Y%m%d_%H%M%S') + '.csv')

    browser.close()

if __name__ == '__main__':
    main()
