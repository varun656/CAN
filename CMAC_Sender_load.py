import can
import codecs
import pickle
import time
import sys
from Crypto.Hash import CMAC
from Crypto.Cipher import DES3


bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
firstmsg = b'start'
lastmsg = b'end'
data = pickle.load( open("random_data.p","rb"))

#text = b'varun123'
#print(text)
#print("Plain text to be encrypted : %s " % text)
secret = b'1122334455667788'
print("Key used for MAC           : %s " % secret)
cobj = CMAC.new(secret, ciphermod=DES3)
msg1 = can.Message(arbitration_id=0x123,data= firstmsg)
bus.send(msg1)

# cobj = CMAC.new(secret, ciphermod=DES3)

start = time.time()
for i in range(int(sys.argv[1])):
    cobj = CMAC.new(secret, ciphermod=DES3)
    cobj.update(data[i])
    mac = cobj.digest()
    #mac_msg = codecs.encode(mac,'hex')
    #print(msg2)
    #bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
    msg = can.Message(arbitration_id=0x123,data = mac)
    msg_t = can.Message(arbitration_id=0x123,data = data[i])
    bus.send(msg)
    #print("Digest key generated       : {} ".format(codecs.encode(mac,'hex')))
    bus.send(msg_t)
    time.sleep(0.003)
    #print("Encrypted Text             : {}".format(codecs.encode(text,'hex')))

end = time.time()
msg2 = can.Message(arbitration_id=0x231,data = lastmsg)
bus.send(msg2)
TimeTaken = end - start
print("The time elapsed to encrypt & send {0} messages : {1} ".format(int(sys.argv[1]),TimeTaken))