import socket
from loguru import logger

# （1）构建服务端套接字对象
sock = socket.socket(family=socket.AF_INET,type = socket.SOCK_STREAM)

sock.connect(('127.0.0.1',8898))


while 1:
    cmd = input("请输入远程执行命令：")

    # （2） 发消息 字节串
    sock.send(cmd.encode())

    if cmd == "exit":
        break

    # (3) 接受消息
    cmd_ret_length_bytes = sock.recv(1024)

    total_size = int(cmd_ret_length_bytes.decode())

    recv_size = 0
    while recv_size < total_size:
        data = sock.recv(1024)
        print(data.decode())
        recv_size += len(data)
    print("recv_size:",recv_size)

    # print("来自服务器的响应结果：", res.decode())

