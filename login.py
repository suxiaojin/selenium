# -*-conding:utf-8 -*-
from selenium import webdriver
import time
def login(username,password):
    driver.get('http://mail.126.com')
    driver.implicitly_wait(8)
    driver.switch_to_frame('x-URS-iframe')
    input=driver.find_element_by_css_selector('[name="email"]')
    input.clear()
    input.send_keys(username)
    pwd=driver.find_element_by_xpath('//*[@class="j-inputtext dlpwd"]')
    pwd.send_keys(password)
    submit=driver.find_element_by_css_selector('#dologin')
    submit.click()
    time.sleep(8)
    driver.switch_to_default_content()
    driver.find_element_by_xpath('//span[contains(text(),"写 信")]').click()

    recive=driver.find_element_by_xpath('//*[@class= "js-component-emailcontainer nui-multiLineIpt C-multiLineIpt nui-ipt"]')
    recive.send_keys('sdsdsd')
 #   driver.find_element_by_css_selector('#_mail_input_2_226').send_keys('auto test')




if __name__=='__main__':
    driver=webdriver.Firefox()
    login("suxiaojin928380","suxiaojin7150915")
