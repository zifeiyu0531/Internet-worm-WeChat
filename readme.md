# Background
Python爬虫爬取微信公众号推文图片（十几万张）

视频地址：[bilibili:【爬虫】爬虫入门(下) 爬取公众号十几万张图片](https://www.bilibili.com/video/BV1Va4y1Y7qy)

本项目目标公众号：全球流行纹身

![image](https://github.com/zifeiyu0531/readme-imgs/blob/master/Internet-worm-WeChat/%E5%85%A8%E7%90%83%E6%B5%81%E8%A1%8C%E7%BA%B9%E8%BA%AB.png)

爬取该公众号`在线查图-风格大全`推文内全部图片，保存至与爬虫程序相同路径下的`图片集`文件夹

![image](https://github.com/zifeiyu0531/readme-imgs/blob/master/Internet-worm-WeChat/%E9%A3%8E%E6%A0%BC%E5%A4%A7%E5%85%A8.jpg)

# Enviroment
浏览器：`Chrome`

浏览器自动化测试驱动：`ChromeDriver`

编程语言：`Python3.7`

第三方爬虫库：`Selenium`

# Install
Chrome：[下载地址](https://www.google.cn/intl/zh-CN/chrome/)

ChromeDriver：[下载地址(淘宝镜像)](http://npm.taobao.org/mirrors/chromedriver/)
```diff
# ChromeDriver版本需与Chrome版本对应
```
Selenium安装：
```
pip install selenium
```
# Usage

# Pack
可使用[PyInstaller](http://www.pyinstaller.org/)将该项目打包成exe格式。<br>
`PyInstaller`安装：
```
pip install pyinstaller
```
使用：
```
pyinstaller -F -w GUI.py
```
在`GUI.py`相同目录下会新增`dist`文件夹，内部放有`GUI.exe`文件