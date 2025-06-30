import  socket
sock = socket.socket()
sock.bind(('127.0.0.1', 8888))
sock.listen(5)


while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print("has data:",data.decode())

    conn.send("HTTP/1.1 200 ok \r\n\r\n<h1>hello</h1>".encode())
    conn.close()