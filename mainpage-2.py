from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
import time
import os
from urllib.request import urlretrieve

url = 'https://mp.weixin.qq.com/mp/homepage?__biz=MzI0MTA2MDk3MA==&hid=28&sn=a9d5bea6dc313eee96a1dd79ab9d5f10&scene=18&devicetype=android-29&version=27000f3d&lang=zh_CN&nettype=WIFI&ascene=7&session_us=gh_f2631d699e12&pass_ticket=4grhxozRhAev9IGqdIFiuiTbY8jJbL4C9zQQ20RQLsW%2BeKOlhG1fjP4%2BE7OcYMoQ&wx_header=1'

browser = webdriver.Chrome()

def get_gage(url):
    try:
        browser.get(url)
        # 获取页面初始高度
        js = "return action=document.body.scrollHeight"
        height = browser.execute_script(js)
        # 将滚动条调整至页面底部
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        #定义初始时间戳（秒）
        t1 = int(time.time())
        # 重试次数
        num=0

        while True:
	        # 获取当前时间戳（秒）
            t2 = int(time.time())
            # 判断时间初始时间戳和当前时间戳相差是否大于2秒，小于2秒则下拉滚动条
            if t2-t1 < 2:
                new_height = browser.execute_script(js)
                if new_height > height :
                    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                    # 重置初始页面高度
                    height = new_height
                    # 重置初始时间戳，重新计时
                    t1 = int(time.time())
                    time.sleep(1)
            elif num < 3:                        # 当超过2秒页面高度仍然没有更新时，进入重试逻辑，重试3次，每次等待2秒
                num = num+1
            else:    # 超时并超过重试次数，程序结束跳出循环，并认为页面已经加载完毕！
                print("滚动条已经处于页面最下方！")
                break
        
        # 获取路径和标题
        links = browser.find_elements_by_class_name('js_post')
        titles = browser.find_elements_by_class_name('js_title')
        
        for i in range(len(links)):
            sub_url = links[i].get_attribute('href')
            title = titles[i].text
            title = title_pre(title)
            print(title)
            print(sub_url)
            # 创建文件夹
            if not os.path.exists('./图片集/'+title):
                os.mkdir('./图片集/'+title)
        
        print("图片下载完成！")
    except Exception as e:
        print(e)     


# 替换文件名中不能出现的字符
def title_pre(title):
    ng_word = ['\\', '/', ':', '：', '*', '?', '？', '\"', '“', '”', '<', '>', '|',]
    for word in ng_word:
        title = title.replace(word, ' ')
    title = title.rstrip()
    return title


get_gage(url)