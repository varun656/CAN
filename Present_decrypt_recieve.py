import can
import time
import os
import codecs
from CryptoPlus.Cipher.pypresent import Present


print('\n\rCAN Rx test')
print('Bring up CAN0....')
os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
time.sleep(0.1)
key = codecs.decode('11223344556677889900','hex')

cipher = Present(key)

try:
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
except OSError:
    print('Cannot find PiCAN board.')
    exit()
    
print('Ready')
print("The present key value is :",key)
try:
    while True:
        message = bus.recv()    # Wait until a message is received.
        
        c = '{0:f} {1:x} {2:x} '.format(message.timestamp, message.arbitration_id, message.dlc)
        s=''
        for i in range(message.dlc ):
            s +=  '{0:x} '.format(message.data[i])
            d = b'message.data[i]'.decode()
            
            
        
        d = bytes.fromhex(s)
        print(d)
        decrypted = cipher.decrypt(d)
        decrypt = codecs.encode(decrypted,'hex')
    
        #print(decrypt)
        print(" The decrypted message is :", decrypt)
        print(' {}'.format(c+s))
        
    
except KeyboardInterrupt:
    #Catch keyboard interrupt
    os.system("sudo /sbin/ip link set can0 down")
    print('\n\rKeyboard interrtupt')
