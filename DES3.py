from Crypto.Cipher import DES3
import pickle
import can
import codecs
import time
import sys

bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

data = pickle.load( open("random_data.p","rb"))

key = "sixteen byte key"
print("The Triple DES key value :",key )
cipher = DES3.new(key, DES3.MODE_ECB) # or 24-byte key

text = [b'varun123', b'message1']
for i in range(2):
    cipher = DES3.new(key, DES3.MODE_ECB)
    encrypted_data = cipher.encrypt(text[i])
    print(encrypted_data)


    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
#decrypt = codecs.encode(decrypted_data,'hex')
    decrypt = codecs.encode(decrypted_data,'hex')
#print(decrypt)
    print(decrypted_data)

    
