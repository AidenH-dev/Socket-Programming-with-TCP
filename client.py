# create an INET, STREAMing socket
import socket


def main():
    # Accept an integer between 1 and 100 from the keyboard
    while True:
        try:
            user_input = int(input("Enter an integer between 1 and 100: "))
            if 1 <= user_input <= 100:
                break
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server (replace 'server_address' and 'port' with actual server details)
    server_address = 'server_address'  # e.g., 'localhost' or '192.168.1.1'
    port = 12345  # replace with the actual port number

    s.connect((server_address, port))

    try:
        # Prepare the message
        name = "Client of Alan Turing"
        message = f"{name},{user_input}"

        # Send data
        s.sendall(message.encode())

        # Look for the response
        response = s.recv(1024)
        print(f"Received: {response.decode()}")

    finally:
        # Close the socket
        s.close()

if __name__ == "__main__":
    main()
