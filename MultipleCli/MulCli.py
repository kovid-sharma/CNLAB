import socket as so
c= so.socket()
port= 7676
c.connect(('localhost',port))

data= input("Enter thr data")
c.send(bytes(data,'utf-8'))
while True:
    print(c.recv(1024).decode())