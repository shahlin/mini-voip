import socket

class MessagingClient:
    SERVER_ADDRESS_PORT = ("127.0.0.1", 20001)
    BUFFER_SIZE = 1024

    def __init__(self):
        # Create a datagram socket
        self.client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    def receive_message(self):
        message = self.client_socket.recvfrom(MessagingClient.BUFFER_SIZE)

        return message[0]

    def send_message(self, bytes_to_send):
        # Send to server using created UDP socket
        self.client_socket.sendto(bytes_to_send, MessagingClient.SERVER_ADDRESS_PORT)