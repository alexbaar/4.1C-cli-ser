import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address and port
server_address = ('localhost', 10000)
sock.bind(server_address)

while True:
    print('\nWaiting for a message from the client...')
    data, client_address = sock.recvfrom(4096)
    print(f'\nReceived message: "{data.decode("utf-8")}" from {client_address}')

    if data.decode('utf-8') == 'Hello':
        response = 'Hello, What’s your name?'
        sock.sendto(response.encode('utf-8'), client_address)

        name_data, _ = sock.recvfrom(4096)
        client_name = name_data.decode('utf-8')
        response = f'Hello {client_name}, Welcome to SIT202'
        sock.sendto(response.encode('utf-8'), client_address)
