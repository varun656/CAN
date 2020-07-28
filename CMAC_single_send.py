import can
import codecs
from Crypto.Hash import CMAC
from Crypto.Cipher import DES3

text = b'varun123'
#print(text)
print("Plain text to be encrypted : %s " % text)
secret = b'1122334455667788'
print("Key used for MAC           : %s " % secret) 
cobj = CMAC.new(secret, ciphermod=DES3)
cobj.update(text)
mac = cobj.digest()
mac_msg = codecs.encode(mac,'hex')
#print(msg2)
bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
msg = can.Message(arbitration_id=0x123,data = mac)
msg1 = can.Message(arbitration_id=0x123,data = text)
bus.send(msg)
print("Digest key generated       : {} ".format(codecs.encode(mac,'hex')))
bus.send(msg1)
print("Encrypted Text             : {}".format(codecs.encode(text,'hex')))