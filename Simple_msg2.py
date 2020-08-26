import can
import time
import os

#os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
#time.sleep(0.1)

#bus2 = can.interface.Bus(channel='can1', bustype='socketcan_native')
bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

'''for message in bus:
    print(message.data)
    d.append(message.data)'''
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
        msgrec.append(d)
        #print(' {}'.format(c+s))
        msg = can.Message(arbitration_id=0x345,data= d)
        bus.send(msg)
        #msgrec.clear()
        
except KeyboardInterrupt:
    #Catch keyboard interrupt
    #os.system("sudo /sbin/ip link set can0 down")
    print('\n\rKeyboard interrtupt')
