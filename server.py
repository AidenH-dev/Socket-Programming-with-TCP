import socket
import random

def start_server(host='10.0.20.6', port=65432):
    server_name = "Server of Grace Hopper"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"{server_name} listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024).decode()
            if data:
                client_name, client_number = data.split(":")
                client_number = int(client_number)
                print(f"Received from {client_name}: {client_number}")
                if 1 <= client_number <= 100:
                    server_number = random.randint(1, 100)
                    total = client_number + server_number
                    print(f"{client_name}, {server_name}, Client Number: {client_number}, Server Number: {server_number}, Sum: {total}")
                    response = f"{server_name}:{server_number}"
                    conn.sendall(response.encode())
                else:
                    print("Received number out of range, shutting down server.")
                    return

if __name__ == "__main__":
    start_server()
