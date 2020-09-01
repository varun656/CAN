import isotp


s = isotp.socket(timeout=10)
s2 = isotp.socket(timeout=10)

s.set_fc_opts(stmin=5, bs=10)

try:
    while True:
        s.bind("can1", isotp.Address(rxid=0x789, txid=0x56))
        s2.bind("can1", isotp.Address(rxid=0x56, txid=0x789))
        print(s.recv())

except KeyboardInterrupt:
    print('\n\rKeyboard interrtupt')