import socket
import threading

# Define server IP and port
IP = '0.0.0.0'
PORT = 9998

def handle_client(client_socket):
    """Handle client connection."""
    with client_socket as sock:
        # Receive data from the client
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        # Send acknowledgment back to the client
        sock.send(b'ACK')

def main():
    """Main server function."""
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))  # Bind to the specified IP and port
    server.listen(5)  # Start listening for incoming connections
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        # Accept a new client connection
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == '__main__':
    main()
