import camellia
plain = b"This is a text ."

#c1 = camellia.CamelliaCipher(key=b'11223344556677881122334455667788', mode=camellia.MODE_ECB)
c1 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
encrypted = c1.encrypt(plain)
print(encrypted.hex)
#c2 = camellia.CamelliaCipher(key=b'16 byte long key', mode=camellia.MODE_ECB)
c2 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
decrypted = c2.decrypt(encrypted)
print(decrypted)