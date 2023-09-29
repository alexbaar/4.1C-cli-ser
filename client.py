import socket
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('localhost', 10000)

time.sleep(2)

# Send initial message to the server
message = 'Hello'
sock.sendto(message.encode('utf-8'), server_address)
print(f'Sent message: "{message}" to the server')

time.sleep(2)

# Receive and display response from the server
response, _ = sock.recvfrom(4096)
print(f'Received message: "{response.decode("utf-8")}" from the server')

# Check if the server is asking for the name
if response.decode('utf-8') == 'Hello, What’s your name?':
    name = input('\nEnter your name: ')
    sock.sendto(name.encode('utf-8'), server_address)
    print(f'Sent name: "{name}" to the server')

time.sleep(2)

# Receive and display the final welcome message from the server
welcome_message, _ = sock.recvfrom(4096)
print(f'\nReceived message: "{welcome_message.decode("utf-8")}" from the server')

# Close the socket
sock.close()
