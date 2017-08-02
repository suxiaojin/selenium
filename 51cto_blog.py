from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver

browser=webdriver.Chrome()
browser.get('http://so.51cto.com')
wait=WebDriverWait(browser,10)

def search():
    input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#q-input > input.text.tips.ui-autocomplete-input')))
    button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#q-input > input.button')))
    input.send_keys('python')
    button.click()

def next_page():
    button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#res-pager > a:nth-child(12)')))
    button.click()

def main():
    search()
    next_page()

if __name__=='__main__':
    main()