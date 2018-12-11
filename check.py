import requests
from bs4 import BeautifulSoup

s=requests.Session()
data=s.get('https://twitter.com')
print(data.headers.get('User-Agent'))
print(data.headers.get('accept'))
print(data.headers.get('accept-language'))
print(data.headers.get('content-type'))
print(data.headers.get('origin'))
print(data.headers.get('referer'))
print(data.headers.get('upgrade-insecure-requests'))
