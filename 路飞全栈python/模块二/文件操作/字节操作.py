# mode =rb
# with open("hello.txt","rb") as f:
#     data = f.read()
#     print(data)
#     print(type(data))
#     print(data.decode("gbk"))

# mode = wb

with open("hello3.txt", "wb") as f:
    f.write("Hello World".encode())