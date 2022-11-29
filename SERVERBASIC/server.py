import socket as so
s= so.socket()
print('Socket made')
port=1234
s.bind(('localhost',port))
s.listen(3)
while True:
    c,addr=s.accept()
    datarecv= c.recv(1024).decode()
    ans=f"the value recieved is {datarecv}"
    print(f"The value recieved is {datarecv}")
    c.send(bytes(ans,'utf-8'))
   