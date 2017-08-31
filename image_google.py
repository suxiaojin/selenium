from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery as pq


def search():
    input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input#lst-ib')))
    input.send_keys('lime')
    input.send_keys(Keys.ENTER)
    get_image()





def get_image():
#    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#rg_s .rg_bx rg_di rg_el ivg-i')))
        html=driver.page_source
        doc=pq(html)

        items=doc('#rg_s .rg_bx rg_di rg_el ivg-i').items()
        for item in items:
            product={
                'url':item.find('.rg_l .rg_ic rg_i').attr('src')
            }
            print(product)
#    except TimeoutException:
#       get_image()






def main():
 #   try:
        search()

 #   finally:
  #      driver.close()

if __name__=='__main__':
    driver = webdriver.Firefox()
    driver.get('https://images.google.com')
    wait = WebDriverWait(driver, 10)
    main()