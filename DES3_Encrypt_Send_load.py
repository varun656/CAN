from Crypto.Cipher import DES3
import pickle
import can
import codecs
import time
import sys

bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
firstmsg = b'start'
lastmsg = b'end'
data = pickle.load( open("random_data.p","rb"))

key = "sixteen byte key"
print("The Triple DES key value :",key )
cipher = DES3.new(key, DES3.MODE_ECB) # or 24-byte key

msg1 = can.Message(arbitration_id=0x123,data= firstmsg)
bus.send(msg1)

start = time.time()
for i in range(10):
    encrypted_data = cipher.encrypt(data[i])
    print(encrypted_data)
    msg = can.Message(arbitration_id=0x123,data= encrypted_data)
    bus.send(msg)
    
end = time.time()
msg2 = can.Message(arbitration_id=0x231,data = lastmsg)
bus.send(msg2)