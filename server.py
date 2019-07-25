import socket
from socket import*
s=socket(AF_INET,SOCK_STREAM)
s.bind(('192.168.0.182',7024))
s.listen(0)
s.settimeout(20)
try:
    c,addr=s.accept()
    c.send(b"hello")
    c.close()
    s.close()
except timeout:
    s.close()