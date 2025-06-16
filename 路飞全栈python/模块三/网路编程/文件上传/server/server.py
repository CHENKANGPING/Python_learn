import socket
from loguru import logger
import json



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
       data_json_bytes = conn.recv(1024)
       file_params = json.loads(data_json_bytes.decode())
       file_name = file_params.get('file_name')
       file_size = file_params.get('file_size')



    with open(f"./upload/{file_name}",'wb') as f:
        receive_data_len = 0
        while receive_data_len < file_size:
            t = conn.recv(1024)
            receive_data_len += len(t)
            f.write(t)

        print("ok")

