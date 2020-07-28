import os
import lz4.frame
import zlib
import codecs

input_data = b'hello' 
print(len(input_data))
compressed = lz4.frame.compress(input_data)
com_hex = codecs.encode(compressed,'hex')
print(compressed)
print(len(compressed))
print(com_hex)

data = b'hello'
print(len(data))
compressed= zlib.compress(data)
print(compressed)
print(len(compressed))
hexdata = codecs.encode(compressed,'hex')
print(hexdata)