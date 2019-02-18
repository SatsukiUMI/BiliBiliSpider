# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 12:29:00 2019

"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
#创建浏览器对象，无头不行
#chrome_options = Options()
#chrome_options.add_argument('--headless')
ua='Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 MicroMessenger/6.3.27 NetType/WIFI Language/zh_CN'
options=webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('user-agent=' + ua)
driver=webdriver.Chrome(options=options)
#driver = webdriver.Chrome(chrome_options=chrome_options)
#driver.get("https://btsow.pw/search/abp-302")
key = str(input('请输入'))
#尝试拼接搜索内容地址
driver.get("https://btsow.pw/search/"+key.lower())
#key = 'ssni-234'
driver.execute_script(
     'window.scrollTo(0,document.body.\
    scrollHeight)')
#等待加载完毕
time.sleep(1)

#开始匹配
#rList = driver.find_elements_by_xpath(
#               '//div[@class="row"]/a')

#c= driver.find_element_by_xpath('//div[@class="row"]/div').text
#print(c)
#print(c.get_attribute('textContent'))

#元素疑似隐藏，测试。
#c= driver.find_element_by_xpath('//div[@class="row"]/a/div[@class="col-xs-12 size-date visible-xs-block"]').is_displayed()
#print(c)
#driver.find_element_by_xpath('//div[@class="row"]/a/div[@class="col-xs-12 size-date visible-xs-block"]')
l = []
for r in driver.find_elements_by_xpath(
               '//div[@class="row"]/a'):
    #str类型
    downlink = r.get_attribute('href')
    title = r.get_attribute('title')
    print(downlink)
    l.append('magnet:?xt=urn:btih:'+downlink[36:])
    l.append(title)

if l == []:
    driver.quit()
    sys.exit('找不到，退出了哦')
    
else:
    file = open("C:\\spyderpj\\HPage\\磁力链接.txt",'a')
    for i in range(len(l)):
        s = str(l[i])
        s = s.replace("'",'').replace(',','') +'\n' 
        file.write(s)
    file.close()
    print('下载完成')
    driver.quit()
