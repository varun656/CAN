import can
import pickle
import codecs
import time
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
for i in range(1000):
    encrypted = cipher.encrypt(data[i])
    msg = can.Message(arbitration_id=0x123,data= encrypted)
    bus.send(msg)
    
end = time.time()
msg2 = can.Message(arbitration_id=0x231,data = lastmsg)
bus.send(msg2)
TimeTaken = end - start
print("The time elapsed to send all message:",TimeTaken)