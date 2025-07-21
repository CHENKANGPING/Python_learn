import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 8080))

sock.listen(5)

while True:
    conn, addr = sock.accept()

    buf = conn.recv(1024)
    print(buf)

    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"hello world")

    conn.close()

sock.close()
