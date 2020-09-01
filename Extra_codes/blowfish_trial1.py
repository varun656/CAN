from Crypto.Cipher import Blowfish
from struct import pack

from Crypto.Cipher import Blowfish
cipher = Blowfish.new("HelloB")
encrypted_data = cipher.encrypt("0123data")
print(encrypted_data)


decrypted_data = cipher.decrypt(encrypted_data)
print(decrypted_data)