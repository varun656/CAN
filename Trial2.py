import codecs
import os
import pickle


msg1 = b'J\x82\x99\xc7\x04Q\x17\xb5'
msg2 = codecs.encode(msg1,'hex')
msg3 = b'123456789'
msg4 = bytearray(msg3)
msg5 = 37 bf 69 9c dc eb 9f b8
msg6 = codecs.decode(msg5, 'hex_codec')
print(msg2)
print(msg4)
print(msg6)

'''data = []
for i in range(30000):
    data.append(os.urandom(8))

pickle.dump( data,open ("random_data.p","wb"))

print(len(data))'''

#os.urandom(8) for _ in range(5)