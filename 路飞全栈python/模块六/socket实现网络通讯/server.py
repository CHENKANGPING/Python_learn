import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 8080))

sock.listen(5)

while True:
    conn, addr = sock.accept()
    conn.sendall("欢迎使用xx系统".encode('utf-8'))
    conn.close()


sock.close()