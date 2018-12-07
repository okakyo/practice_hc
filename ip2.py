import socket,socks,requests 

class Tor:
    def __init__(self):
        ip='localhost'
        port=9050
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS,ip,port)
        socket.socket=socket.socksocket

    def get_ip(self):
        s=requests.sessin()
        try:
            ip_addr=s.get('https://api.ipify.org/').text
            return ip_addr
        except socks.ProxyConnectionError:
            print("[*]Proxy Error")

        return

if __name__=='__main__':
    Tor=Tor()
    ip=Tor.get_ip()
    print(ip)
