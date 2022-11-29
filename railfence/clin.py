'''import socket as so
client= so.socket()
port= 1234
def encryptRailFence(text, key):
rail = [['\n' for i in range(len(text))]
for j in range(key)]
dir_down = False
row, col = 0, 0
for i in range(len(text)):
if (row == 0) or (row == key - 1):
dir_down = not dir_down
rail[row][col] = text[i]
col += 1
if dir_down:
row += 1
else:
row -= 1
result = []
for i in range(key):
for j in range(len(text)):
if rail[i][j] != '\n':
result.append(rail[i][j])
return("" . join(result))
client.connect(('localhost',port))
id= input('Enter the data you want to encrypt: ')
key= input('Enter key: ')
key= int(key)
encrypted= encryptRailFence(id,key)
client.send(bytes(encrypted,'utf-8'))
ans=client.recv(1024).decode()'''
