import  socket
sock = socket.socket()
sock.bind(('127.0.0.1', 8888))
sock.listen(5)


while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print("has data")

    conn.send("HTTP/1.1 200 ok \r\n\r\nhello".encode())
    conn.close()