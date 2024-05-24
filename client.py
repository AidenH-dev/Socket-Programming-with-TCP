# create an INET, STREAMing socket
import socket


server_name = 'localhost'
port = 8080

print("Connecting to {server_name}, PORT: {port} ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_name, port))
print(f"Just connected to {client.getpeername()}")

message = f"Hello from {client.getsockname()}"
client.sendall(message.encode('utf-8'))

response = client.recv(1024)
print(f"Received: {response.decode('utf-8')}")

client.close()



