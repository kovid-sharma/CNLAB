'''import socket as so
s=so.socket()
print("Socket is now built")
port=1234
s.bind(('localhost', port))
s.listen(3)
print('Waiting for Connection')
def decryptRailFence(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
    for j in range(key)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
    if row == 0:
    dir_down = True
    if row == key - 1:
    dir_down = False
    rail[row][col] = '*'
    col += 1
    if dir_down:
    row += 1
    else:
    row -= 1
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
                                        (index < len(cipher))):
                rail[i][j] = cipher[index]
    index += 1
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
        dir_down = True
        if row == key-1:
        dir_down = False
        if (rail[row][col] != '*'):
        result.append(rail[row][col])
        col += 1
        if dir_down:
        row += 1
        else:
        row -= 1
    return("".join(result))
while True:
    c,addr= s.accept()
    datarecv=c.recv(1024).decode()
    key=input("Enter the key value used fro decryption")
    change= decryptRailFence(datarecv,int(key))
    c.send(bytes(f"{change} is the decryption of the data recieved using the given key -> {key}
    ",'utf-8'))'''
