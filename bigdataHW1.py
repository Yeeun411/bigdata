from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


def kyochon_store(result):
    Kyochon_URL = "http://www.kyochon.com/shop/domestic.asp"
    wd = webdriver.Chrome('C:/Users/kang-yeeun/Desktop/chromedriver.exe')

    wd.get(Kyochon_URL)
    time.sleep(1)

    sidoSelect = wd.find_element(By.CSS_SELECTOR, "#sido1")

    for siIndex, sido in enumerate(sidoSelect.find_elements(By.CSS_SELECTOR, "option")):
        sidoSelect = wd.find_element(By.CSS_SELECTOR, "#sido1")
        sido = sidoSelect.find_elements(By.CSS_SELECTOR, "option")[siIndex]
        sido.click()
        time.sleep(1)
        sidoTxt = sido.text

        gugunSelect = wd.find_element(By.CSS_SELECTOR, "#sido2")
        for guIndex, gu in enumerate(gugunSelect.find_elements(By.CSS_SELECTOR, "option")):
            gugunSelect = wd.find_element(By.CSS_SELECTOR, "#sido2")
            gu = gugunSelect.find_elements(By.CSS_SELECTOR, "option")[guIndex]
            gu.click()
            time.sleep(1)
            gugunTxt = gu.text
            wd.execute_script("search();")
            time.sleep(2)

            store_list = wd.find_elements(By.CSS_SELECTOR, "ul.list > li")
            for store in store_list:
                try:
                    name = store.find_element(By.CSS_SELECTOR, "strong").text
                    address = store.find_element(By.CSS_SELECTOR, "em").text
                    result.append([name, sidoTxt, gugunTxt, address])
                    print(name, sidoTxt, gugunTxt, address)
                except NoSuchElementException:
                    continue

def main():
    result = []
    print('Kyochon store crawling >>>>>>>>>>>>>>>>>>>>>>>>')
    kyochon_store(result)

    kyochon_tbl = pd.DataFrame(result, columns=('store', 'sido', 'gugun', 'address'))
    kyochon_tbl.to_csv('./bigDataHW1.csv', encoding='cp949', mode='w', index=True)
    print("success")


if __name__ == '__main__':
    main()
