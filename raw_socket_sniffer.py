import sys, socket, struct, binascii
try:
    raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

except socket.error as e:
    print(e)
    sys.exit()

while True:
    packet = raw_socket.recvfrom(2048)
    ethernet_header = packet[0][:14]
    eth_header = struct.unpack("!6s6s2s", ethernet_header)
    print("Ethernet Header --- \nDestination: " + str(binascii.hexlify(eth_header[0])) + "\n Source: " + str(binascii.hexlify(eth_header[1])) + "\n Type: " + str(binascii.hexlify(eth_header[2])) + "\n")
    ip_header = packet[0][14:34]
    ip_head = struct.unpack("!12s4s4s", ip_header)
    print("IP Header -- \nDestination: " + str(binascii.hexlify(ip_head[0])) + "\n Source: " + str(binascii.hexlify(ip_head[1])) + "\n Type: " + str(binascii.hexlify(ip_head[2])) + "\n")