import isotp
import time
import os
import codecs



print('\n\rCAN ISO-TP test')
print('Bring up CAN1....')
#os.system("sudo /sbin/ip link set can1 up type can bitrate 500000")
time.sleep(0.1)

s = isotp.socket()
s2 = isotp.socket()
s.set_fc_opts(stmin=5, bs=10)

s3 = isotp.socket()
s4 = isotp.socket()
s3.set_fc_opts(stmin=5, bs=10)

s5 = isotp.socket()
s6 = isotp.socket()
s6.set_fc_opts(stmin=5, bs=10)


print('Ready')
#time1 = []
count = 0
try:
    while True:
        count += 1
        s.bind("can1", isotp.Address(rxid=0x123, txid=0x45))
        s2.bind("can1", isotp.Address(rxid=0x45, txid=0x123))     
        if s.recv() == b'start':
            start = time.time()
            continue;
        s5.bind("can0", isotp.Address(rxid=0x123, txid=0x47))
        s6.bind("can0", isotp.Address(rxid=0x47, txid=0x123))
        if s5.recv() == b'end':
            end = time.time()
            break;
        s3.bind("can0", isotp.Address(rxid=0x123, txid=0x46))
        s4.bind("can0", isotp.Address(rxid=0x46, txid=0x123))
        print(" The received message is :", s3.recv())
        #print(' {}\n'.format(c+s))

              
    
except KeyboardInterrupt:
    #Catch keyboard interrupt
    #os.system("sudo /sbin/ip link set can1 down")
    print('\n\rKeyboard interrtupt')
count = count - 2
TimeTaken = end - start
print("The time taken to receive '{0}' message(s): {1}".format(count,TimeTaken))