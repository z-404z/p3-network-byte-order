import sys
import socket

def check_endian():
    if sys.byteorder == "little":
        print("Your system is Little-Endian.")
    else:
        print("Your system is Big-Endian.")

def convert_integer():
    data = eval(input())
    print(f"Original (Decimal): {data}")
    print(f"Original (Hex): {hex(data)}")
    network_32 = socket.htonl(data)
    host_32 = socket.ntohl(network_32)
    print(f"32-bit => Host to Network: {hex(network_32)}, Network to Host: {hex(host_32)}")
    network_16 = socket.htons(data)
    host_16 = socket.ntohs(network_16)
    print(f"16-bit => Host to Network: {hex(network_16)}, Network to Host: {hex(host_16)}")

if __name__ == "__main__":
    check_endian()
    print("\nPerforming integer conversion...")
    convert_integer()
