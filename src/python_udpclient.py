import socket

msgFromClient       = ""
serverAddressPort   = ("127.0.0.1", 7501)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


def send_equipment_code(equipment_code):
    msgFromClient = equipment_code
    bytesToSend = str.encode(msgFromClient)
    
    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = (UDPClientSocket.recvfrom(bufferSize)[0]).decode("utf-8")
    msg = f"Message from Server: \"{msgFromServer}\""

    print(msg)