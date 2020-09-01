from Crypto.Cipher import Salsa20

plain_text = b'Hello'
secret= b'1122334455667788'
cipher = Salsa20.new(key=secret)
msg = cipher.nonce + cipher.encrypt(plain_text)

print(msg[:8])