# FileName == "zippasscracker.py"
# Author   == "PawanKumar {SmartxCodes}"
# Language == "Python --version3.8"
# Youtube  == "https://www.youtube.com/SmartxCoodes"
# Use      == "to crack zip file"
import zipfile, os
import time
from time import sleep
from tqdm import tqdm

print("FileName == zippasscracker.py")
print("Author   == PawanKumar {SmartxCodes}")
print("Language == Python --version3.8")
print("Youtube  == https://www.youtube.com/SmartxCoodes")
print("Use      == to crack zip file")

zfile = input("Zip File <path|file.zip> :- ")
wfile = input("Password File <path|file.txt> :- ")

zip_file = zipfile.ZipFile(zfile)
n_words = len(list(open(wfile,"rb")))

print("Total Passwords to test : ",n_words)

with open(wfile, "rb") as wordlist:
    for word in tqdm(wfile,tatal=n_words,unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password Found : ", word.decode.strip())
            exit(0)
