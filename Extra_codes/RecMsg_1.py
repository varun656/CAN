import can
import time
import os
import codecs


print('\n\rCAN Rx test')
print('Bring up CAN0....')
os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
time.sleep(0.1) 

try:
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
except OSError:
    print('Cannot find PiCAN board.')
    exit()
    
print('Ready')
time1 = []
try:
    while True:
        message = bus.recv()    # Wait until a message is received.
        
        c = '{0:f} {1:x} {2:x} '.format(message.timestamp, message.arbitration_id, message.dlc)
        s=''
        for i in range(message.dlc ):
            s +=  '{0:02X} '.format(message.data[i])
            #d = b'message.data[i]'.decode()
            
            
        #d = codecs.decode(s,'hex_codec')
        
        #d = bytes.fromhex(s).decode('utf-8')
        #d = bytearray(s)
        d = bytearray.fromhex(s)
        
        print(' {}'.format(c+s) )
        #time.sleep(0.1)
        #time1.append(message.timestamp)
        #diff = [time1[i+1]-time1[i] for i in range(len(time1)-1)]
        #print(sum(diff))
        if d == b'start':
           start = time.time() 
        if d == b'end':
            end = time.time()
            break;

except KeyboardInterrupt:
    #Catch keyboard interrupt
    #os.system("sudo /sbin/ip link set can0 down")
    print('\n\rKeyboard interrtupt')

TimeTaken = end - start
print(TimeTaken)
    