import socket

from loguru import logger

import subprocess

# （1）构建服务端套接字对象
sock = socket.socket(family=socket.AF_INET,type = socket.SOCK_STREAM)

# （2）bind listen accept

sock.bind(('127.0.0.1',8898))
sock.listen(5)
logger.info("服务器启动，等待连接")

while 1:
    logger.info("等待连接")
    conn, addr = sock.accept()
    # print(f"conn{conn},addr{addr}")
    logger.info(f"来自于客户端{addr}的请求成功")

    while 1:
        # (3)收消息
        cmd_bytes = conn.recv(1024)

        print("cmd:", cmd_bytes.decode())

        if cmd_bytes == 'exit'.encode() or len(cmd_bytes) == 0:
            logger.info(f"来自于{addr}客户端退出")
            break

        # (4) 处理数据
        cmd_ret = subprocess.getoutput(cmd_bytes.decode())
        if not cmd_ret:
            cmd_ret = "执行完毕！"

        # 发送数据长度
        cmd_ret_length = str(len(cmd_ret.encode()))
        conn.send(cmd_ret_length.encode())

        # 发送数据
        conn.send(cmd_ret.encode())