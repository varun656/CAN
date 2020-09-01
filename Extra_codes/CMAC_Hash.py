from Crypto.Hash import CMAC
from Crypto.Cipher import DES3, AES
secret = b'1122334455667788'
cobj = CMAC.new(secret, ciphermod=DES3)
cobj.update(b'varun123')
mac = cobj.digest()
print(mac)

secret2 = b'1122334455667788'
cobj2 = CMAC.new(secret, ciphermod=DES3)
cobj2.update(b'varun123')
#mac2 = cobj2.digest()
#print(mac2)
#print(cobj2.hexdigest())
try:
    cobj2.verify(mac)
    print("The message is authentic")
except ValueError:
    print("The message is not authentic")
