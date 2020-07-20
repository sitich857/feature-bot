from socket import *
from multiprocessing import Process
ADDR=("0.0.0.0", 8888)
def handle(connfd):
    while True:
        data=connfd.recv(1024)
        if not data:
            break
        print(data)
        connfd.send(b'thank#')
    connfd.close
def main():
    sock=socket()
    sock.bind(ADDR)
    sock.listen(5)

    while True:
        connfd,addr=sock.accept()

        p=Process(target=handle,args=(connfd,))
        p.daemon=True
        p.start()