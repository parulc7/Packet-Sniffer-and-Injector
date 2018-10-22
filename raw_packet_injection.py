import sys, socket, struct

try:
    raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

except socket.error as t:
    print(t)
    sys.exit()

raw_socket.bind(("wlo1", socket.htons(0x0800)))
packet = struct.pack("!6s6s2s",b'\xb8v?\x8b\xf5\xfe',b'l\x19\x8f\xe1J\x8c', b'\x08\x00')
raw_socket.send(packet)

