def encrypt(text,key):
    ans=""
    for c in text:
        if(c==' '):
            ans+=' '
        else:
            ans+= chr(((ord(c)-97)+key+26)%26 +97)
    return ans
text= input("Enter the text you want to encrypt : ")
key= int(input("Enter the key used for encryption : "))
print("The encrypted text is " + encrypt(text,key))
print("The decrypted text is " + encrypt(encrypt(text,key),-key))