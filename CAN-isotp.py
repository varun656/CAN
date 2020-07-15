import isotp

s = isotp.socket()
s2 = isotp.socket()
# Configuring the sockets.
s.set_fc_opts(stmin=5, bs=10)
#s.set_general_opts(...)
#s.set_ll_opts(...)

s.bind("can0", isotp.Address(rxid=0x123, txid=0x45))
s2.bind("can0", isotp.Address(rxid=0x45, txid=0x123))
s2.send(b"hello hi how are you im good everything will be fine ")
print(s.recv())