import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    url = 'https://www.baidu.com/'
    url = 'http://www.taobao.com'
    url = 'https://www.bilibili.com/'
    driver = webdriver.Firefox()
    driver.get(url)
    print(type(driver))
    # print(driver.page_source)

    # input = driver.find_element(By.ID,value='q')
    # input.send_keys('ipad')
    # time.sleep(1)
    # input.clear()
    # input.send_keys('iphone')
    # click = driver.find_element(By.CLASS_NAME,'btn-search')
    # click.click()


    # print(a)

    time.sleep(500)

if __name__ == '__main__' :
    main()

"""
driver.find_element(By.XPATH, '//*[@id="kw"]') 
# 根据xpath选择元素(万金油)
driver.find_element(By.CSS_SELECTOR, '#kw') 
# 根据css选择器选择元素
driver.find_element(By.NAME, 'wd') 
# 根据name属性值选择元素
driver.find_element(By.CLASS_NAME, 's_ipt') 
# 根据类名选择元素
driver.find_element(By.LINK_TEXT, 'hao123') 
# 根据链接文本选择元素
driver.find_element(By.PARTIAL_LINK_TEXT, 'hao') 
# 根据包含文本选择
driver.find_element(By.TAG_NAME, 'title') 
# 根据标签名选择
# 目标元素在当前html中是唯一标签或众多标签第一个时候使用
driver.find_element(By.ID, 'su') 
# 根据id选择
"""
