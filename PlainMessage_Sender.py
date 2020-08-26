import can
import pickle
import codecs
import time
import sys


bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
firstmsg = b'start'
lastmsg = b'end'
text = sys.argv[1]

print("The plain text entered is    :",text)

start = time.time()

plain = bytearray(sys.argv[1],'utf-8');


encrypt = codecs.encode(plain,'hex')
print("The plain text in hex is :",encrypt)

msg1 = can.Message(arbitration_id=0x231,data= firstmsg)
bus.send(msg1)


msg = can.Message(arbitration_id=0x123,data= plain)
bus.send(msg)
    
end = time.time()
msg2 = can.Message(arbitration_id=0x231,data = lastmsg)
bus.send(msg2)
TimeTaken = end - start
print("The time elapsed to send '{0}' message : {1} ".format(sys.argv[1],TimeTaken))