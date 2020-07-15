import can
from Crypto.Hash import CMAC
from Crypto.Cipher import DES3

secret = b'1122334455667788'
cobj = CMAC.new(secret, ciphermod=DES3)
cobj.update(b'varun123')
msg3 = cobj.digest()
print(cobj.hexdigest())
print(msg3)
#print(msg2)
bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
msg = can.Message(arbitration_id=0x00,data = msg3)
bus.send(msg)