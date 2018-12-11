import requests
from bs4 import BeautifulSoup

s=requests.session()
headers={}

response=s.get('https://twitter.com/',headers=headers,allow_redirects=True)
soup=BeautifulSoup(response.text,'lxml')
auth_token=soup.find(attrs={'name':'authenticity_token'}).get("value")
print('authentiency_token: '+auth_token)
print('Status_Code:{}'.format(response.status_code))
