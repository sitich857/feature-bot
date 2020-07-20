from threading import Thread
from socket import *
from signal import *

ADDR = ("0.0.0.0", 8888)


def func(connfd):
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        msg = "thanks"
        connfd.send(msg.encode())
    connfd.close()


def main():
    sockfd = socket()
    sockfd.bind(ADDR)
    sockfd.listen(5)

    while True:
        try:
            connfd, addr = sockfd.accept()
        except:
            sockfd.close()
            return

        t = Thread(target=func, args=(connfd,))
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    main()
