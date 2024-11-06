import socket

# socket setup
def setup_receive_socket(ip, recv_port):
    receive_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    receive_socket.bind((ip, recv_port))
    return receive_socket

# code handlers
def handle_code202(broadcast_socket, address):
    print("Code 202 received; game starting")
    send_message(broadcast_socket, "202", address)

def handle_code221(broadcast_socket, address, count):
    if count < 2:
        return count + 1
    print("Game ending")
    send_message(broadcast_socket, "221", address)
    return 0

def handle_code53(broadcast_socket, address):
    print("Code 53 received - Red base scored")
    send_message(broadcast_socket, "53", address)

def handle_code43(broadcast_socket, address):
    print("Code 43 received - Green base scored")
    send_message(broadcast_socket, "43", address)

def send_message(socket, message, address):
    msg = str.encode(str(message))
    socket.sendto(msg, address)

def main():
    ip = "127.0.0.1"
    recv_port = 7501
    buffer_size = 1024
    serverAddressPort   = ("127.0.0.1", 7500)

    # initialize sockets
    receive_socket = setup_receive_socket(ip, recv_port)
    broadcast_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    count = 0

    try:
        while True:
            # receive message and address from port 7501
            bytes_address_pair = receive_socket.recvfrom(buffer_size)
            message, address = bytes_address_pair
            message = message.decode("utf-8")

            print(f"Client Message: \"{message}\"")
            print(f"Client IP Address: {address}")

            if message == '202':
                handle_code202(broadcast_socket, serverAddressPort)
            elif message == '221':
                count = handle_code221(broadcast_socket, serverAddressPort, count)
            elif message == '53':
                handle_code53(broadcast_socket, serverAddressPort)
            elif message == '43':
                handle_code43(broadcast_socket, serverAddressPort)
            else:
                send_message(broadcast_socket, message, serverAddressPort)

    except KeyboardInterrupt:
        print("Server is shutting down")
    finally:
        receive_socket.close()
        broadcast_socket.close()

if __name__ == "__main__":
    main()
