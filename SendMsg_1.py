import can
import pickle
import codecs
import time

#can_msg = [b'1122334455667788', b'98765432' ]
#print(can_msg)
#text = bytearray([1,2,3])
#text = b'\x04I\xce\x16\x92\xd0\xb6\x9c'
bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
#msg = can.Message(arbitration_id=0x00,data=[45, 25, 0, 1, 3, 8, 9, 16])
#msg = can.Message(arbitration_id=0x123,data= text)
#bus.send(msg)
firstmsg = b'start'
lastmsg = b'end'
data = pickle.load( open("random_data.p","rb"))
msg100 = codecs.encode(data[99], 'hex')
msg1000 = codecs.encode(data[1000], 'hex')
data.pop(5)
msg1 = can.Message(arbitration_id=0x123,data= firstmsg)
bus.send(msg1)
#print(data[1])
#print(len(data))
print(data[:10])
start = time.time()
for i in range(10):
    msg = can.Message(arbitration_id=0x123,data= data[i])
    #time.sleep(0.1)
    bus.send(msg)
end = time.time()
msg2 = can.Message(arbitration_id=0x231,data = lastmsg)
bus.send(msg2)
TimeTaken = end - start
print(TimeTaken)
#print