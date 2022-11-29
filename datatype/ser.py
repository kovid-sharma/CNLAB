import socket as so
s= so.socket()

port= 3234

s.bind(('localhost',port))


s.listen(3)


print('Server is Listening...')
while True:
    cl,addr= s.accept()

    data= cl.recv(1024).decode()

    currData='INT'

    for c in data:
        if(c=='-' or c==')'):
            currData='Special Character'
            break
    for c in data:
        if(c>='a' or c<='z' or c>='A' or c<='Z'):
            currData='String'
            break
    if(len(data)==1 and currData=='String'):
        currData='Character'
    ans= f"The data type of the sent data is {currData}"
    cl.send(bytes(currData,'utf-8'))    
    also= cl.recv(1024).decode()
    data=also
    currData='INT'

    for c in data:
        if(c=='-' or c==')'):
            currData='Special Character'
            break
    for c in data:
        if((c>='a' and c<='z') or (c>='A' and c<='Z')):
            currData='String'
            break
    if(len(data)==1 and currData=='String'):
        currData='Character'
    ans= f"The data type of the sent data is {currData}"
    cl.send(bytes(currData,'utf-8'))
    