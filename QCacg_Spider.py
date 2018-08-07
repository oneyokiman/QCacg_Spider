#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import os
import re
import sys
#      自己的第一次Python爬虫尝试
server = "https://www.qcacg.com/"
target = input('输入想要爬的QC轻小说网址，\n 回车默认为《为了成功的恋爱，作战吧》：')
if target :
	pass
else :	
	target = 'https://www.qcacg.com/catalog/114'
a = requests.get(url = target)#抓取目录页的网页源码
bf = BeautifulSoup(a.text)#创建BeautifulSoup对象
tags = bf.findAll('div', class_ = 'group')
book_name_ = bf.findAll('div',class_ = 'clear')
b = BeautifulSoup(str(tags))
c = b.findAll('a')#查找class下的标签a
os.mkdir('C:\\Users\\Administrator\\Desktop\\已下载小说')#新建文件夹用于储存爬取的文章
os.chdir('C:\\Users\\Administrator\\Desktop\\已下载小说')#进入文件夹
for each in c :
	url = each.get('href')#获取页码后缀
	target = 'https://www.qcacg.com%s' %(url)#前缀+后缀
	req = requests.get(url = target)#获取内容页的网页源码
#	html = req.text	#读取数据
	bf = BeautifulSoup(req.text)#创建BeautifulSoup对象
	texts = bf.find_all('div', class_ = 'book-content')#BF分析并查找关键字眼
	book_name = each.get('title')
	fp = open('%s.txt'%(book_name),'w',encoding = 'utf-8')#新建一个.txt文件
	str = texts[0].text + '\n'
	print('正在下载%s'%(book_name))
	fp.write(str)#写入数据