import socket as so
s= so.socket()
port= 7676
s.bind(('localhost',port))

s.listen(3)
userlist=[]
def brod(c,data):
    for d in userlist:
        if(c!=d)
            d.send(bytes(data,'utf-8'))
print("Server is Listening...")
while True:
    c,addr= s.accept()
    data= c.recv(1024).decode()
    userlist.append(c)
    brod(c,data)
    print(data)
    #c.send(bytes(data,'utf-8'))
