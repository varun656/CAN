import can
import time
import os
import codecs
from Crypto.Cipher import Blowfish
from struct import pack


print('\n\rCAN Rx test')
print('Bring up CAN0....')
os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
time.sleep(0.1)
key = b'1122334455667788'
print("The Blowfish encryption key is :", key)
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

try:
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
except OSError:
    print('Cannot find PiCAN board.')
    exit()
    
print('Ready')

try:
    while True:
        message = bus.recv()    # Wait until a message is received.
        
        c = '{0:f} {1:x} {2:x} '.format(message.timestamp, message.arbitration_id, message.dlc)
        s=''
        for i in range(message.dlc ):
            s +=  '{0:x} '.format(message.data[i])
            d = b'message.data[i]'.decode()
            
        d = bytes.fromhex(s)
        decrypted_data = cipher.decrypt(d)
        
        
        #print(decrypt)
        #print(" The decrypted message is :", decrypt)
        print(' {}'.format(c+s))
        print("The decrypted msg is: ", decrypted_data)
        
    
except KeyboardInterrupt:
    #Catch keyboard interrupt
    os.system("sudo /sbin/ip link set can0 down")
    print('\n\rKeyboard interrtupt')

