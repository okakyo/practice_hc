import requests
from bs4 import BeautifulSoup

s=requests.session()
headers={}

response=s.get('',headers=headers,allow_redirection=True)
soup=BeautifulSoup(response,'lxml')
auth_token=soup.find(atters={'name':'authentiency_token'}).get('value')
print('authentiency_token: '+auth_token)
print('Status_Code:{}'.format(response.status_code))
