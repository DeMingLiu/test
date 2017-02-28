#!/usr/bin/python 
#coding:utf8
import re
import urllib
def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read()
  return html
def getImg(html):
  reg = r'src="(.*?\.JPEG)" '
  imgre = re.compile(reg)
  imglist = re.findall(imgre,html)
  x = 0
  for imgurl in imglist:
    urllib.urlretrieve(imgurl,'%s.jpg' % x)
    x += 1
  print x
html = getHtml("https://www.baidu.com/")
getImg(html)