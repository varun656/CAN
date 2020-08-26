import can
import pickle
import codecs
import time
import sys
from CryptoPlus.Cipher.pypresent import Present

bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
firstmsg = b'start'
lastmsg = b'end'
text = sys.argv[1]


key = codecs.decode('11223344556677889900','hex')
print("The Present key value        :",key )
print("The plain text entered is    :",text)
cipher = Present(key)

start = time.time()

plain = bytearray(sys.argv[1],'utf-8');
print(plain)
encrypted = cipher.encrypt(plain)
encrypt = codecs.encode(encrypted,'hex')
print("The encrypted text in hex is :",encrypt)

msg1 = can.Message(arbitration_id=0x231,data= firstmsg)
bus.send(msg1)


msg = can.Message(arbitration_id=0x123,data= encrypted)
bus.send(msg)
    
end = time.time()
msg2 = can.Message(arbitration_id=0x231,data = lastmsg)
bus.send(msg2)
TimeTaken = end - start
print("The time elapsed to encrypt & send '{0}' message : {1} ".format(sys.argv[1],TimeTaken))