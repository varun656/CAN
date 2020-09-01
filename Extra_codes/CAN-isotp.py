import isotp
from Crypto.Cipher import DES3

s = isotp.socket()
s2 = isotp.socket()
# Configuring the sockets.
s.set_fc_opts(stmin=5, bs=10)
#s.set_general_opts(...)
#s.set_ll_opts(...)
text = b'varun123'
key = "sixteen byte key"
print("The Triple DES key value :",key )
cipher = DES3.new(key, DES3.MODE_ECB)
encrypted_data = cipher.encrypt(text)

s.bind("can0", isotp.Address(rxid=0x123, txid=0x45))
s2.bind("can0", isotp.Address(rxid=0x45, txid=0x123))
s2.send(encrypted_data)
print(s.recv())