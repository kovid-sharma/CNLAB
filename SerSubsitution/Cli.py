import socket as so
client= so.socket()
port= 1234
data= input('Enter the data you want to check whose data type: ')
client.connect(('localhost',port))
client.send(bytes(data,'utf-8'))
print(client.recv(1024).decode())