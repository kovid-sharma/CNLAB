import socket as so
client= so.socket()
port= 12345
data= input('Enter the data you want to check whose data type: ')
key= input("enter the key")
data= data+key
client.connect(('localhost',port))
client.send(bytes(data,'utf-8'))
print(client.recv(1024).decode())