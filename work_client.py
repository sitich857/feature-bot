from socket import *

sockfd = socket()
sockfd.connect(('localhost', 8889))
f = open("liubei.jpg", "rb")
data = f.read()
sockfd.send(data)

sockfd.close()
