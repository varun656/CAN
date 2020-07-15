from simon import SimonCipher

#my_simon = SimonCipher(0xABBAABBAABBAABBAABBAABBAABBAABBA)
tiny_cipher = SimonCipher(0x123456789ABCDEF0, key_size=72, block_size=48)
my_plaintext = bytes([0x11, 0x22, 0x33])
simon_ciphertext = tiny_cipher.encrypt(my_plaintext)
print(simon_ciphertext)
simon_plaintext = tiny_cipher.decrypt(simon_ciphertext)
print(simon_plaintext)
a = simon_plaintext.decode("hex")

print(a)