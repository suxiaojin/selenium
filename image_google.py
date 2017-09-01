from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery as pq
import time
import requests
import os
from hashlib import md5
from requests.exceptions import RequestException



def search():
    input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input#lst-ib')))
    input.send_keys('lime')
    input.send_keys(Keys.ENTER)
    get_image()


def get_image():
    pos=0
    for i in range(10):
        pos+=i*500
        js="var q=document.documentElement.scrollTop=%d" %pos
        driver.execute_script(js)
        time.sleep(3)

    html=driver.page_source
    doc = pq(html)
    item=doc('div.rg_bx:nth-child(1)')
    url=item.find('.rg_l .rg_ic').attr('src')

def download_image(url):
    print('正在下载:',url)
    try:
        response=requests.get(url)
        if response.status_code==200:
            save_images(response.content)
        return None
    except RequestException:
        print('请求图片出错')
        return None


def save_images(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()




def main():

        search()


if __name__=='__main__':
    driver = webdriver.Firefox()
    driver.get('https://images.google.com')
    wait = WebDriverWait(driver, 10)
    main()