import socket
import threading

from loguru import logger


def conn_handler(conn):
    while 1:
        # (3)收消息
        data_bytes = conn.recv(1024)

        print("data:", data_bytes.decode())

        if data_bytes == 'exit'.encode() or len(data_bytes) == 0:
            logger.info(f"来自于{addr}客户端退出")
            break

        # (4) 处理数据
        data = data_bytes.decode()
        res = data.upper()
        conn.send(res.encode())


# （1）构建服务端套接字对象
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# （2）bind listen accept

sock.bind(('127.0.0.1', 8890))
sock.listen(5)
logger.info("服务器启动，等待连接")

while 1:
    logger.info("等待连接")
    conn, addr = sock.accept()
    # print(f"conn{conn},addr{addr}")
    logger.info(f"来自于客户端{addr}的请求成功")

    # 创建一个客户端的线程对象
    t = threading.Thread(target=conn_handler, args=(conn,))
    t.start()
