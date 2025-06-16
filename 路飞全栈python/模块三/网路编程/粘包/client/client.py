import  socket

s = socket.socket()

s.connect(('127.0.0.1',8898))

data = input(">>>")

s.send(data.encode())
s.send(data.encode())
s.send(data.encode())

res = s.recv(1024)
print(res)







