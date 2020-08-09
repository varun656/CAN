import can
import pickle
import codecs
import time
import sys
from Crypto.Cipher import Blowfish

bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
firstmsg = b'start'
lastmsg = b'end'
data = pickle.load( open("random_data.p","rb"))

bs = Blowfish.block_size
key = b'1122334455667788'
print("The Blowfish encryption key is :", key)
cipher = Blowfish.new(key, Blowfish.MODE_ECB)


msg1 = can.Message(arbitration_id=0x123,data= firstmsg)
bus.send(msg1)

start = time.time()
for i in range(int(sys.argv[1])):
    encrypted = cipher.encrypt(data[i])
    msg = can.Message(arbitration_id=0x123,data= encrypted)
    bus.send(msg)
    
end = time.time()
msg2 = can.Message(arbitration_id=0x231,data = lastmsg)
bus.send(msg2)
TimeTaken = end - start
print("The time elapsed to encrypt & send {0} messages : {1} ".format(int(sys.argv[1]),TimeTaken))