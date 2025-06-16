import json
import socket
from loguru import logger
import os
# （1）构建服务端套接字对象
sock = socket.socket(family=socket.AF_INET,type = socket.SOCK_STREAM)

sock.connect(('127.0.0.1',8898))


while 1:
    inp = input("命令：")

    local_path = inp.split(" ")[1]
    file_name = os.path.basename(local_path)
    file_size = os.path.getsize(local_path)
    file_params = {"file_name":file_name,"file_size":file_size}


    sock.send(json.dumps(file_params).encode())


    with open(local_path,"rb") as f:
        for line in f:
            sock.send(line)


    print("ok")





