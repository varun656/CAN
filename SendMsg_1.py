import can
import pickle
import codecs 
#can_msg = [b'1122334455667788', b'98765432' ]
#print(can_msg)
#text = bytearray([1,2,3])
#text = b'\x04I\xce\x16\x92\xd0\xb6\x9c'
bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
#msg = can.Message(arbitration_id=0x00,data=[45, 25, 0, 1, 3, 8, 9, 16])
#msg = can.Message(arbitration_id=0x123,data= text)
#bus.send(msg)

data = pickle.load( open("random_data.p","rb"))
msg100 = codecs.encode(data[99], 'hex')
msg1000 = codecs.encode(data[1000], 'hex')
#print(data[1])
#print(len(data))
print(msg100)
print(msg1000)
for i in range(100):
    msg = can.Message(arbitration_id=0x123,data= data[i])
    bus.send(msg)
#print