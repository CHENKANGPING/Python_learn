import socket
from loguru import logger

# （1）构建服务端套接字对象
sock = socket.socket(family=socket.AF_INET,type = socket.SOCK_STREAM)

sock.connect(('127.0.0.1',8890))


while 1:
    name = input("请输入转换的姓名：")

    # （2） 发消息 字节串
    sock.send(name.encode())

    if name == "exit":
        break

    # (3) 接受消息
    res = sock.recv(1024)

    print("来自服务器的响应消息", res.decode())

