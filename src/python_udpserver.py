import socket

localIP     = "127.0.0.1"
localPort   = 7501
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

count = 0

def code202Received():
    print("Code 202 received; game starting")
    return

def code221Received():
    if count == 0:
            count += 1
            return
    elif count == 1:
        count += 1
        return
    elif count == 2:
        print("Game ending")
        count = 0 
        return
    return

def code53Received():
    print("Code 53 received")
    #If code 53 is received, the red base has been scored.
    #If the player is on the green team, they will receive 100 points and a stylized letter "B" will be added to the left of their codename.
    return
    
def code43Received():
    print("Code 43 received")
    #If code 43 is received, the green base has been scored
    #If the player is on the red team, they will receive 100 points and a stylized letter "B" will be added to the left of their codename.
    

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)
       
    # receiving codes
    receivedCode = message.decode('utf-8')
    
    if receivedCode == '202':
        code202Received()
    elif receivedCode == '221':
        code221Received()
    elif receivedCode == '53':
        code53Received()
    elif receivedCode == '43':
        code43Received()

    msgFromServer = f"Received equipment code: {message}"
    bytesToSend = str.encode(msgFromServer)
    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)