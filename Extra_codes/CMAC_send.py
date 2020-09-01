import RPi.GPIO as GPIO
import can
import time
import os
from Crypto.Hash import CMAC
from Crypto.Cipher import DES3


secret = b'1122334455667788'
cobj = CMAC.new(secret, ciphermod=DES3)
msg2 = cobj.update(b'varun123')
#print(cobj.hexdigest())
msg3 = cobj.digest()

led = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,True)

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
        msg = can.Message(arbitration_id=0x7de,data = msg3,extended_id=False)
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
