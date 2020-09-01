import zlib
import codecs

data = "varun123"
compressed= zlib.compress(data)
print(compressed)
hexdata = codecs.encode(compressed,'hex')
print(hexdata)