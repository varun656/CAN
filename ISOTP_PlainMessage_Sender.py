import isotp
import pickle
import codecs
import time
import sys


s = isotp.socket()
s2 = isotp.socket()
s.set_fc_opts(stmin=5, bs=10)

s3 = isotp.socket()
s4 = isotp.socket()
s3.set_fc_opts(stmin=5, bs=10)

s5 = isotp.socket()
s6 = isotp.socket()
s6.set_fc_opts(stmin=5, bs=10)

firstmsg = b'start'
lastmsg = b'end'
text = sys.argv[1]

print("The plain text entered is    :",text)

start = time.time()

plain = bytearray(sys.argv[1],'utf-8');


encrypt = codecs.encode(plain,'hex')
print("The plain text in hex is :",encrypt)

s.bind("can0", isotp.Address(rxid=0x123, txid=0x45))
s2.bind("can0", isotp.Address(rxid=0x45, txid=0x123))
s2.send(firstmsg)

s3.bind("can0", isotp.Address(rxid=0x123, txid=0x46))
s4.bind("can0", isotp.Address(rxid=0x46, txid=0x123))
s4.send(plain)

    
end = time.time()
s5.bind("can0", isotp.Address(rxid=0x123, txid=0x47))
s6.bind("can0", isotp.Address(rxid=0x47, txid=0x123))
s6.send(lastmsg)
TimeTaken = end - start
print("The time elapsed to send '{0}' message : {1} ".format(sys.argv[1],TimeTaken))