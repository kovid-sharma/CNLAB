import socket as so
s=so.socket()
port=12345
s.bind(('localhost',port))

s.listen(3)

while True:
    c,addr= s.accept()
    data= c.recv(1024).decode()
    print(f"the data is {data}")
    ans= f"the data is {data}"
    c.send(bytes(ans,'utf-8'))

