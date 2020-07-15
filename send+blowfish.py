import RPi.GPIO as GPIO
import can
import time
import os
import sys
from Crypto.Cipher import Blowfish
from struct import pack


led = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,True)
#msg1 = b'dea

#msg1 = [0x00,0x01,0x02,0x03]
#msg1 = 0xdd,0x0e,0x0a,0x0d,0x0b,0x0e,0x0e,0x0f
#for i in range(1,len(sys.argv)):
#    msg1.append(int(sys.argv[i]))
#msg1 = bytearray(sys.argv[1],'utf-8');
#msg1= b'pJ\xe63qJ\x83\x94'
#msg1 = [hex(x) for x in msg1]
#msg1 = [hex(int(i,16)) for i in msg1]
#msg1 = [1,2]
bs = Blowfish.block_size
key = b'Hello'
cipher = Blowfish.new(key, Blowfish.MODE_ECB)
plaintext = b'varun12'
plen = bs - len(plaintext) % bs
padding = [plen]*plen
padding = pack('b'*plen, *padding)
msg2 = cipher.encrypt(plaintext + padding)
#print(msg1)

print(msg2)

#msg2 = bytearray(b"message")
#print(msg2)

count = 0

print('\n\rCAN Rx test')
print('Bring up CAN0....')

# Bring up can0 interface at 500kbps
os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
time.sleep(0.1) 
print('Press CTL-C to exit')

try:
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
except OSError:
    print('Cannot find PiCAN board.')
    GPIO.output(led,False)
    exit()

# Main loop
try:
    while True:
        GPIO.output(led,True)   
        msg = can.Message(arbitration_id=0x7de,data=msg2,extended_id=False)
        bus.send(msg)
        count +=1
        time.sleep(0.1)
        GPIO.output(led,False)
        time.sleep(0.1) 
        print(count)    
         

    
except KeyboardInterrupt:
    #Catch keyboard interrupt
    GPIO.output(led,False)
    os.system("sudo /sbin/ip link set can0 down")
    print('\n\rKeyboard interrtupt')

