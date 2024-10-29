import socket

# socket setup
def setup_broadcast_socket(ip, send_port):
    broadcast_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    broadcast_socket.bind((ip, send_port))
    return broadcast_socket

def setup_receive_socket(ip, recv_port):
    receive_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    receive_socket.bind((ip, recv_port))
    return receive_socket

# code handlers
def handle_code202(broadcast_socket, address):
    print("Code 202 received; game starting")
    send_message(broadcast_socket, "Game starting", address)

def handle_code221(broadcast_socket, address, count):
    if count < 2:
        return count + 1
    print("Game ending")
    send_message(broadcast_socket, "Game ending", address)
    return 0

def handle_code53(broadcast_socket, address):
    print("Code 53 received - Red base scored")
    send_message(broadcast_socket, "Red base scored", address)

def handle_code43(broadcast_socket, address):
    print("Code 43 received - Green base scored")
    send_message(broadcast_socket, "Green base scored", address)

def send_message(socket, message, address):
    msg = str.encode(message)
    socket.sendto(msg, address)

def main():
    ip = "127.0.0.1"
    send_port = 7500
    recv_port = 7501
    buffer_size = 1024

    # initialize sockets
    broadcast_socket = setup_broadcast_socket(ip, send_port)
    receive_socket = setup_receive_socket(ip, recv_port)

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
                handle_code202(broadcast_socket, address)
            elif message == '221':
                count = handle_code221(broadcast_socket, address, count)
            elif message == '53':
                handle_code53(broadcast_socket, address)
            elif message == '43':
                handle_code43(broadcast_socket, address)
            else:
                # message is a player's equipment code
                msg_from_server = f"Received equipment code: {message}"
                send_message(broadcast_socket, msg_from_server, address)

    except KeyboardInterrupt:
        print("Server is shutting down")
    finally:
        broadcast_socket.close()
        receive_socket.close()

if __name__ == "__main__":
    main()
