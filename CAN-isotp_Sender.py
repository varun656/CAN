import isotp


s = isotp.socket()
s2 = isotp.socket()

s.set_fc_opts(stmin=5, bs=10)

text = b'The module allows to send big chunks of data by establishing a point to point connection and sending large chunk data'


s.bind("can0", isotp.Address(rxid=0x789, txid=0x56))
s2.bind("can0", isotp.Address(rxid=0x56, txid=0x789))
s2.send(text)
print("The message transmitted using CAN-ISOTP module is :",s.recv())