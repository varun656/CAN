from Crypto.Cipher import Blowfish
from struct import pack

bs = Blowfish.block_size
key = b'Hello'
cipher = Blowfish.new(key, Blowfish.MODE_ECB)
plaintext = b'varun123'
plen = bs - len(plaintext) % bs
padding = [plen]*plen
padding = pack('b'*plen, *padding)
msg = cipher.encrypt(plaintext + padding)
print(msg)