
import hashlib
from tabnanny import check
from time import sleep


print("Hey You are Currentyl Using File Integrity Monitoring Software which helps you in maintaining the integrity of your files")
 
print (" _   _            _   __        __            _ ")
print ("| | | | __ _  ___| | _\ \      / /__  ___  __| |")
print ("| |_| |/ _` |/ __| |/ /\ \ /\ / / _ \/ _ \/ _` |")
print ("|  _  | (_| | (__|   <  \ V  V /  __/  __/ (_| |")  
print ("|_| |_|\__,_|\___|_|\_\  \_/\_/ \___|\___|\__,_|")
print ("                                                ")

filepath = input("Please Enter The File Path: ")

def gethash(filepath):
    sha256 = hashlib
    with open(filepath,'rb') as file:
        hashes = file.read()
        sha256.update(hashes)
        return sha256.hexdigest()

BaseLine = gethash(filepath)
sleep(0.50)
print("[*] Checking Your Files and Calculating the hashes")
sleep(0.25)
print("[*]Calculating... ")
sleep(.25)
print("[*]Please Wait")

while True:
    check = gethash(filepath)
    if check != BaseLine:
        print("[*] Your Files have Been Changed or Edited") 
        sleep(0.25)
    else:
        print("Your File Is Safe Till Now")
        sleep(2)
    
