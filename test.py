from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
browser=webdriver.Chrome()
browser.get('http://www.baidu.com')
time.sleep(3)
#元素定位：find_element_by_id()
#browser.find_element_by_id('kw').send_keys('python')

#元素定位：find_element_by_name()
#browser.find_element_by_name('wd').send_keys('python')

#元素定位：find_element_by_class_name()
#browser.find_element_by_class_name('s_ipt').send_keys('json')

#元素定位：find_element_by_tag_name() 每个元素的tag(标签)属性
#browser.find_element_by_tag_name('input').send_keys('selenium')

#元素定位：find_element_by_link_text(),定位到页面上的链接，并点击
#browser.find_element_by_link_text('hao123').click()



#元素定位：find_element_by_xpath()通过id来定位
#browser.find_element_by_xpath('//*[@id="kw"]').send_keys('xpath')
#元素定位：find_element_by_xpath()通过name来定位
#browser.find_element_by_xpath('//*[@name="wd"]').send_keys('xpath name')
#元素定位：find_element_by_xpath()通过class属性来定位
#browser.find_element_by_xpath('//*[@class="s_ipt"]').send_keys('xpath class')
#元素定位：find_element_by_xpath()通过其它属性来定位
#browser.find_element_by_xpath('//*[@autocomplete="off"]').send_keys('xpath 属性')
#元素定位：find_element_by_xpath()有时候同一个属性，同名的比较多，这时候可以通过标签筛选下，定位更准一点
#browser.find_element_by_xpath('//input[@id="kw"]').send_keys('xpath')
#元素定位：find_element_by_xpath()通过父节点属性来定位
#browser.find_element_by_xpath('//span[@id="s_kw_wrap"]/input').send_keys('xpath')
#元素定位：find_element_by_xpath()通过爷爷节点属性来定位
# browser.find_element_by_xpath('//form[@id="form"]/span/input').send_keys('xpath')



#css用#号表示id属性，  css用.表示class属性，  css直接用标签名称
#元素定位：find_element_by_css_selector()通过id属性来定位
#browser.find_element_by_css_selector('#kw').send_keys('xpath css')
#元素定位：find_element_by_css_selector()通过class属性来定位
#browser.find_element_by_css_selector('.s_ipt').send_keys('xpath css')

#元素定位：find_element_by_css_selector()通过标签与属性的组合来定位
# browser.find_element_by_css_selector('input.s_int')
# browser.find_element_by_css_selector('input#kw')
#元素定位：find_element_by_css_selector()通过属性值
#find_element_by_css_selector("[name='wd']")
#css同样也可以实现逻辑运算，同时匹配两个属性，这里跟xpath不一样，无需写and关键字
#find_element_by_css_selector('.nui-ipt-input''[maxlength="256"]')
'''

在做web应用的自动化测试时，定位元素是必不可少的，这个过程经常会碰到定位不到元素的情况（报selenium.common.exceptions.NoSuchElementException），一般可以从以下几个方面着手解决：
1.Frame/Iframe原因定位不到元素：
　　这个是最常见的原因，首先要理解下frame的实质，frame中实际上是嵌入了另一个页面，而webdriver每次只能在一个页面识别，因此需要先定位到相应的frame，对那个页面里的元素进行定位。
解决方案：
如果iframe有name或id的话，直接使用switch_to_frame("name值")或switch_to_frame("id值")。如下：
driver=webdriver.Firefox()
driver.get(r'http://www.126.com/')
driver.switch_to_frame('x-URS-iframe')  #需先跳转到iframe框架
username=driver.find_element_by_name('email')
username.clear()
'''

'''
iframe定位：

iframe的切换是默认支持id和name的方法的，当然实际情况中会遇到没有id属性和name属性为空的情况，这时候就需要先定位iframe
driver.switch_to.frame(driver.find_element_by_class_name('APP-editor-iframe'))
当iframe上的操作完后，想重新回到主页面上操作元素，这时候，就可以用switch_to.default_content()方法返回到主页面
'''

'''
chrome操作js，操作滚动条
js = "var q=document.body.scrollTop=0"
driver.execute_script(js)
'''

'''
firefox操作js，操作滚动条

滚动条回到顶部：

js="var q=document.getElementById('id').scrollTop=0"
driver.execute_script(js）
2.滚动条拉到底部

js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)

3.这里可以修改scrollTop 的值，来定位右侧滚动条的位置，0是最上面，10000是最底部。
'''

#获取cookies
#print(browser.get_cookies())
#browser.get_cookies(name="cnblogscookie")

#q清除指定的cookie
#browser.delete_cookie(name=".cnblogcookie")

#刷新页面
#browser.refresh()


# 添加cookie的值
# add_cookie(cookie_dict)



# #设置窗口大小540*960

# browser.set_window_size(540,960)
# time.sleep(3)

# #窗口最大化
# browser.maximize_window()

# # browser.get('http://www.163.com')
# # time.sleep(3)

# # #返回上一页
# # browser.back()
# # time.sleep(3)

# # #切换到下一页
# # browser.forward()
browser.quit()