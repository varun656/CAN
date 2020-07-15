import codecs
from CryptoPlus.Cipher.pypresent import Present
key = codecs.decode('11223344556677889900','hex')
#key = "00000000000000000000".decode('hex')
#plain = "0000000000000000".decode('hex')
#for i in range
count=1
while count < 100000:
    text = "1010" & count
    plain = codecs.decode(text,'hex')
    cipher = Present(key)
    encrypted = cipher.encrypt(plain)
    encrypt = codecs.encode(encrypted,'hex')
    print("The encrypted text is : ",encrypt)

decrypted = cipher.decrypt(encrypted)
decrypt = codecs.encode(decrypted,'hex')
print("The decrypted text is : ",decrypt)

#encrypted.encode('hex')