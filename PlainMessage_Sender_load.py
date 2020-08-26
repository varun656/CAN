import can
import pickle
import codecs
import time
import sys


bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
firstmsg = b'start'
lastmsg = b'end'
data = pickle.load( open("random_data.p","rb"))


msg1 = can.Message(arbitration_id=0x123,data= firstmsg)
bus.send(msg1)

start = time.time()
for i in range(int(sys.argv[1])):
    msg = can.Message(arbitration_id=0x123,data= data[i])
    bus.send(msg)
    
end = time.time()
msg2 = can.Message(arbitration_id=0x231,data = lastmsg)
bus.send(msg2)
TimeTaken = end - start
print("The time elapsed to send {0} message(s) : {1} ".format(int(sys.argv[1]),TimeTaken))