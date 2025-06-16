import  socket
import  time

s = socket.socket()
s.bind(('127.0.0.1', 8898))
s.listen(5)

client,addr = s.accept()
time.sleep(10)
data = client.recv(1024)
print(data)

client.send(data)