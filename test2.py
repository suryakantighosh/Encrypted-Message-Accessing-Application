##########created by Mr. Suryakanti Ghosh####################



#two synchronous and asynchornus

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from datetime import datetime
import os
import mysql.connector as c

con = c.connect(host ="localhost", user = "root", passwd = "admin", database = "encryption_app")
cur = con.cursor()


def encrypt_aes(plaintext, key):
    # Generate a random 16-byte IV
    iv = os.urandom(16)
    
    # Create a cipher object using the key and iv
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Pad the plaintext to be a multiple of the block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    
    # Encrypt the padded plaintext
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    return iv + ciphertext  # Prepend IV to the ciphertext

def decrypt_aes(ciphertext, key):
    # Extract the IV from the beginning of the ciphertext
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    
    # Create a cipher object using the key and iv
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Decrypt the ciphertext
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Unpad the plaintext
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    
    return plaintext
print("------------------Welcome to Encrypted Message accessing application-------------------")
while True:
    print('''enter a choice
    1. encrytption
    2. decryption
    3. exit
    choice ->''', end = ' ')
    ch = int(input())
    if ch == 1:
        print("enter the text to be encrypted", end = "\n")
        text = input()
        print("enter the username -->", end = "\t")     
        username = input()
        print("enter the one time password -->  ")
        passwd = input()
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        key  = os.urandom(32)
        ciphertext = encrypt_aes(text.encode('utf-8'), key)
        try:
            cmd = "INSERT INTO app_data (date, data, aes_key, username, psswd) VALUES (%s,%s,%s,%s,%s)"
            cur.execute(cmd,(time,ciphertext,key,username,passwd))
            con.commit()
            print("your msg is saved")
        except Exception as e:
            print(e)
    elif ch ==2 :
        print("enter the username -->  ")
        username1 = input()
        print("enter the one time password -->  ")
        passwd1 = input()
        try:
            cmd = "select date, data, aes_key, username , psswd from app_data where username = '{}'".format(username1)
            cur.execute(cmd)
            row = cur.fetchone()
            if row != None:
                date = row[0]
                ciphertext = row[1]
                key = row[2]
                username2 = row[3]
                passwd2 = row[4]
                if passwd1 == passwd2 :
                    decrypted_text = decrypt_aes(ciphertext, key)
                    decrypted_text = decrypted_text.decode('utf-8')
                    print(f"Decrypted text = {decrypted_text}")
                    cmd = "delete from app_data where username ='{}'".format(username1)
                    cur.execute(cmd)
                    con.commit()
                    print("entry deleted succesfully from Server")
                else:
                    print("wrong password")
            else:
                print(f"No entries found with username -> {username1}")    
        except Exception as e:
            print(e)

    elif ch == 3:
        print("------------------------Thank you visit again----------------------")
        break
    else:
        print("INVALID CHOICE, please enter a valid option")
