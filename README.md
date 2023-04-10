# Multimedia-information-retrieval
## 系统框架
基于Djabgo框架
## 爬取
爬取应用了下面几个库：
import re
import requests
from urllib import error
from bs4 import BeautifulSoup
## 检索算法
使用感知哈希算法，缩小图片到32*32，进行DCT计算
计算DCT就DCT把图片分离成分率的集合，再计算缩小DCT后的所有像素点的平均值，得到信息指纹，数值越小则越相似
## 前端设计框架
bootstrap框架，通过form表单获取用户输入信息
