import can
import time
import os
import codecs
from Crypto.Hash import CMAC
from Crypto.Cipher import DES3


secret = b'1122334455667788'
print("Receiver's key used for MAC : %s " % secret) 

cobj = CMAC.new(secret, ciphermod=DES3)
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

try:
    msg = []
    while True:
        message = bus.recv()    # Wait until a message is received.
        cobj = CMAC.new(secret, ciphermod=DES3)
        c = '{0:f} {1:x} {2:x} '.format(message.timestamp, message.arbitration_id, message.dlc)
        s=''
        for i in range(message.dlc ):
            s +=  '{0:02X} '.format(message.data[i])
            d = b'message.data[i]'.decode()
            
            
        
        d = bytes.fromhex(s)
        msg.append(d)
        print(' {}'.format(c+s))
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

