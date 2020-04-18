import socket

class MessagingServer:
    LOCAL_IP = "127.0.0.1"
    LOCAL_PORT = 20001

    BUFFER_SIZE = 1024

    def __init__(self):
        # Create a datagram socket
        self.server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        # Bind to address and ip
        self.server_socket.bind((MessagingServer.LOCAL_IP, MessagingServer.LOCAL_PORT))
    
    def receive_message(self):
        bytes_address_pair = self.server_socket.recvfrom(MessagingServer.BUFFER_SIZE)
        message = bytes_address_pair[0]
        address = bytes_address_pair[1]

        return (message, address)

    def send_message(self, bytes_to_send, address_to_send_to):
        # Sending a reply to client
        self.server_socket.sendto(bytes_to_send, address_to_send_to)