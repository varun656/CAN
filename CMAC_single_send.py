import can
import codecs
import time
import sys
from Crypto.Hash import CMAC
from Crypto.Cipher import DES3

firstmsg = b'start'
lastmsg = b'end'
plain = sys.argv[1]

print("Plain text to be encrypted :",plain)
secret = b'1122334455667788'
print("Key used for MAC           :",secret)

start = time.time()

text = bytearray(sys.argv[1],'utf-8');
cobj = CMAC.new(secret, ciphermod=DES3)
cobj.update(text)
mac = cobj.digest()
mac_msg = codecs.encode(mac,'hex')

bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

msgs = can.Message(arbitration_id=0x123,data = firstmsg)
bus.send(msgs)

msg = can.Message(arbitration_id=0x123,data = mac)
msg1 = can.Message(arbitration_id=0x123,data = text)
bus.send(msg)
print("Digest key generated       : {} ".format(codecs.encode(mac,'hex')))
bus.send(msg1)
print("Encrypted Text             : {}".format(codecs.encode(text,'hex')))
end = time.time()

msge = can.Message(arbitration_id=0x123,data = lastmsg)
bus.send(msge)
TimeTaken = end - start
print("The time elapsed to encrypt & send '{0}' message : {1} ".format(sys.argv[1],TimeTaken))