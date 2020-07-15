import codecs

msg1 = b'\xc7\xe1\x8a\xaa\xe7?\xa2\x8a'
msg2 = codecs.encode(msg1,'hex')
print(msg2)