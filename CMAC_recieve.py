import can
import time
import os
import codecs
from Crypto.Hash import CMAC
from Crypto.Cipher import DES3


secret = b'1122334455667788'
print("Receiver's key used for MAC : ",secret) 

cobj = CMAC.new(secret, ciphermod=DES3)
#print('\n\rCAN Rx test')
print('Bring up CAN1....')
os.system("sudo /sbin/ip link set can1 up type can bitrate 500000")
time.sleep(0.1)


try:
    bus = can.interface.Bus(channel='can1', bustype='socketcan_native')
except OSError:
    print('Cannot find PiCAN board.')
    exit()
count = 0
try:
    msg = []
    while True:
        message = bus.recv()
        count += 1
        cobj = CMAC.new(secret, ciphermod=DES3)
        c = '{0:f} {1:x} {2:x} '.format(message.timestamp, message.arbitration_id, message.dlc)
        s=''
        for i in range(message.dlc ):
            s +=  '{0:02X} '.format(message.data[i])
            d = b'message.data[i]'.decode()
            
            
        
        d = bytes.fromhex(s)
        if d == b'start':
            start = time.time()
            continue;
        if d == b'end':
            end = time.time()
            break; 
        msg.append(d)
        #print(' {}'.format(c+s))
        if len(msg) == 2:
            cobj.update(msg[1])
            mac = msg[0]
            try:
                cobj.verify(mac)
                print("The message is authentic :%s " % msg[1])
                msg.clear()
            except ValueError:
                print("The message is not authentic")
                msg.clear()
        
    
        #print(decrypt)
        #print(decrypt)
        #print(' {}'.format(c+s))
        
    
except KeyboardInterrupt:
    #Catch keyboard interrupt
    #os.system("sudo /sbin/ip link set can0 down")
    print('\n\rKeyboard interrtupt')
count = (count - 2)/2
TimeTaken = end - start
print("The time taken to receive & decrypt {0} messages: {1}".format(count,TimeTaken))

