import codecs
import os
import pickle

msg1 = b'\xc7\xe1\x8a\xaa\xe7?\xa2\x8a'
msg2 = codecs.encode(msg1,'hex')
msg3 = b'123456789'
msg4 = bytearray(msg3)
print(msg2)
print(msg4)

data = []
for i in range(9000):
    data.append(os.urandom(8))

pickle.dump( data,open ("random_data.p","wb"))

print(len(data))

#os.urandom(8) for _ in range(5)