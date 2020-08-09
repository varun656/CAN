import can
import time
import os

bus = can.interface.Bus(channel='can1', bustype='socketcan_native')
listener = SomeListener()

msg = bus.recv()

listener.on_message_received(msg)
print(msg.data)


listener.stop