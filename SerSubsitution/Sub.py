import socket as so
s=so.socket()
port=12345
s.bind(('localhost',port))
def encrypt(text,key):
    ans=""
    for c in text:
        if(c==' '):
            ans+=' '
        else:
            ans+= chr(((ord(c)-97)+key+26)%26 +97)
    return ans

print("Server is Listening...")
s.listen(3)

while True:
    c,addr= s.accept()
    data= c.recv(1024).decode()
    print(f"the data is {data}")
    hehe= data[-1:]
    hehe= int(hehe)
    text= data[0:len(data)-1]
    print(text)
    print("The encrypted text is " + encrypt(text,hehe))
    print("The decrypted text is " + encrypt(encrypt(text,hehe),-hehe))
    

