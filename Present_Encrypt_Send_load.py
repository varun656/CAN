import can
import pickle
import codecs
import time
import sys
from CryptoPlus.Cipher.pypresent import Present

bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
firstmsg = b'start'
lastmsg = b'end'
data = pickle.load( open("random_data.p","rb"))


key = codecs.decode('11223344556677889900','hex')
print("The Present key value :",key )
cipher = Present(key)

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