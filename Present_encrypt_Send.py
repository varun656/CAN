import RPi.GPIO as GPIO
import can
import time
import os
import codecs
from CryptoPlus.Cipher.pypresent import Present

led = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,True)

count = 0

key = codecs.decode('11223344556677889900','hex')
print("The Present key value :",key )
text = "deadbeefdeadbeef"
print("The plain text is : ",text)
plain = codecs.decode(text,'hex')
cipher = Present(key)
encrypted = cipher.encrypt(plain)
encrypt = codecs.encode(encrypted,'hex')
print("The encrypted text is : ",encrypt)

print('\n\rCAN Tx test')
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
        msg = can.Message(arbitration_id=0x7de,data=encrypted,extended_id=False)
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
