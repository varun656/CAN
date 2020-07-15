import can
bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
msg = can.Message(arbitration_id=0x00,data=[45, 25, 0, 1, 3, 8, 9, 16])
bus.send(msg)