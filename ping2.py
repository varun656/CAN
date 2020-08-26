import can
import time
import os
import sys



ping = bytearray(sys.argv[1],'utf-8');
os.system("python3 ~/Documents/CAN/Simple_msg2.py &")
print("   Ping Test   ")
print("Message sent            :", sys.argv[1]) 
start = time.time()
bus = can.interface.Bus(channel='can1', bustype='socketcan_native')
msg = can.Message(arbitration_id=0x123,data = ping)
bus.send(msg)
msgrec = []
try:
    #msgrec = []
    while len(msgrec) < 1:
        message = bus.recv()    # Wait until a message is received.
        
        c = '{0:f} {1:x} {2:x} '.format(message.timestamp, message.arbitration_id, message.dlc)
        s=''
        for i in range(message.dlc ):
            s +=  '{0:x} '.format(message.data[i])
            d = b'message.data[i]'.decode()
            
        d = bytes.fromhex(s)
        end = time.time()
        msgrec.append(d)
        print("Message recieved        :", d)
        TimeTaken = end - start
        print("Total time for TX/RX is :",TimeTaken)
except KeyboardInterrupt:
    print('\n\rKeyboard interrtupt')
