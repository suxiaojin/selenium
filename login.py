# -*-conding:utf-8 -*-
from selenium import webdriver
import time
def login(username,password):
    driver.get('http://mail.126.com')
    driver.implicitly_wait(8)
    driver.switch_to.frame('x-URS-iframe')
    input=driver.find_element_by_css_selector('[name="email"]')
    input.clear()
    input.send_keys(username)
    pwd=driver.find_element_by_xpath('//*[@class="j-inputtext dlpwd"]')
    pwd.send_keys(password)
    submit=driver.find_element_by_css_selector('#dologin')
    submit.click()
    time.sleep(8)
    #跳出框架
    driver.switch_to.default_content()
    driver.find_element_by_xpath('//span[contains(text(),"写 信")]').click()
    #收件人地址
    driver.find_element_by_xpath('//*[@class="nui-editableAddr-ipt"]').send_keys(r'suxiaojin928380@sina.com')
    #邮件主题
    driver.find_element_by_css_selector('.nui-ipt-input''[maxlength="256"]').send_keys('auto test2')

    #这里是在正文输入框中写内容,有iframe框架，所以需要进入框架先
    driver.switch_to.frame(driver.find_element_by_class_name('APP-editor-iframe'))
    driver.find_element_by_css_selector('.nui-scroll').send_keys('this is a text email2')
    # 跳出框架
    driver.switch_to.default_content()
    driver.find_element_by_xpath('//span[contains(text(),"发送") and @class="nui-btn-text"]').click()
    try:
        assert '发送成功' in driver.page_source
    except AssertionError:
        print('邮件发送成功')
    else:
        print('邮件发送失败')


if __name__=='__main__':
    driver=webdriver.Firefox()
    login("suxiaojin928380","suxiaojin7150915")
