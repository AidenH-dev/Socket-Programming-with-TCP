import socket

def start_client(host='10.0.20.6', port=65432):
    client_name = "Client of Alan Turing"
    client_number = int(input("Enter an integer between 1 and 100: "))
    if not (1 <= client_number <= 100):
        print("Number out of range. Exiting.")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        message = f"{client_name}:{client_number}"
        s.sendall(message.encode())
        
        data = s.recv(1024).decode()
        if data:
            server_name, server_number = data.split(":")
            server_number = int(server_number)
            total = client_number + server_number
            print(f"Received from {server_name}: {server_number}")
            print(f"{client_name}, {server_name}, Client Number: {client_number}, Server Number: {server_number}, Sum: {total}")

if __name__ == "__main__":
    start_client()
