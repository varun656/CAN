import can
import time
import os
import codecs
from CryptoPlus.Cipher.pypresent import Present


print('\n\rCAN Rx test')
#print('Bring up CAN0....')
os.system("sudo /sbin/ip link set can1 up type can bitrate 500000")
time.sleep(0.1)
key = codecs.decode('11223344556677889900','hex')

cipher = Present(key)

try:
    bus = can.interface.Bus(channel='can1', bustype='socketcan_native')
except OSError:
    print('Cannot find PiCAN board.')
    exit()
    
print('Ready')
print("The present key value is :",key)
#time1 = []
count = 0
try:
    while True:
        message = bus.recv()    # Wait until a message is received.
        count += 1
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
        decrypted = cipher.decrypt(d)
        decrypt = codecs.encode(decrypted,'hex')
        print(" The decrypted message is :", decrypt)
        #print(' {}\n'.format(c+s))

        
        
    
except KeyboardInterrupt:
    #Catch keyboard interrupt
    os.system("sudo /sbin/ip link set can1 down")
    print('\n\rKeyboard interrtupt')
count = count - 2
TimeTaken = end - start
print("The time taken to receive & decrypt {0} messages: {1}".format(count,TimeTaken))
