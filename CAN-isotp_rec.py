import isotp

s = isotp.socket(timeout=10)
s2 = isotp.socket(timeout=10)
# Configuring the sockets.
s.set_fc_opts(stmin=5, bs=10)
#s.set_general_opts(...)
#s.set_ll_opts(...)


try:
    while True:
        s.bind("can1", isotp.Address(rxid=0x123, txid=0x45))
        s2.bind("can1", isotp.Address(rxid=0x45, txid=0x123))
        print(s.recv())

except KeyboardInterrupt:
    print('\n\rKeyboard interrtupt')