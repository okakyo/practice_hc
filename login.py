import requests,sys
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

class TwitterLogin:
    def __init__(self):
        self.username='ideatrain.waterlily@gmail.com '
        self.password='d6r5Wz8u'

    def login(self):
        s=requests.Session()
        headers={
                "User-Agent":"Mozilla/5.0",              
                "accept":"text/html,application/xhtml+xml,application/xml;",              
                "accept-language":"ja en-US;q=0.8,en=0.6",
                "content-type":"application/x-www-form-urlencoded",              
                "origin":"https://twitter.com",
                "referer":"https://twitter.com",
                "upgrade-insecure-requests":"1"
                }

        payload={
                "session[username_or_email]":"",
                "session[password]":"",
                "remember_me":"1",
                "return_to_ssl":"true",
                "scribe_log":"",
                "redirect_after_login":"/"
                }

        try:
            response=s.get("https://twitter,com/",headers=headers,allow_redirects=False)
            soup=BeautifulSoup(response.text,'lxml')
            auth_token=soup.find(attrs={'name':'authenticity_token'}).get('value')

        except ConnectionError:
            print("[*] Twitter cannot connected!")
            sys.exit()

        payload["authenticity-token"]=auth_token
        payload["session[username_or_email]"]=self.username
        payload["session[password]"]=self.password

        try:
            login=s.post("https://twitter,com/sessions",headers=headers,data=payload,allow_redirects=False)
            if login.status_code==302:
                print(login.status_code)
            else:
                print(login.status_code)
        except:
            pass

if __name__=='__main__':
    twitter=TwitterLogin()
    twitter.login()
