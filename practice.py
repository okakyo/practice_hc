import requests
import socket
import socks
import os,sys
import base64
import bs4 import BeautifulSoup

url=''
s=requests.session()
data=s.get(url)

#print(data.content())
soup=BeautifulSoup(data,encoding='UTF-8')
print(soup.prettify())

