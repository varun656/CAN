import can
import pickle
import codecs
import time
import sys
from Crypto.Cipher import Blowfish

bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
firstmsg = b'start'
lastmsg = b'end'
text = sys.argv[1]

bs = Blowfish.block_size
key = b'1122334455667788'
print("The Blowfish encryption key is :", key)
cipher = Blowfish.new(key, Blowfish.MODE_ECB)
print("The plain text entered is    :",text)


start = time.time()

plain = bytearray(sys.argv[1],'utf-8');
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