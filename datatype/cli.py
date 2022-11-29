import socket as so

client= so.socket()


port= 3234


client.connect(('localhost',port))

data= input('Enter the data you want to check')

client.send(bytes(data,'utf-8'))
while True:
    print(client.recv(1024).decode())
    data= input('Enter the data you want to check')
    client.send(bytes(data,'utf-8'))

    