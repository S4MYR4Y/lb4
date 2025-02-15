# Echo server implementation
import socket

def handle_client(conn, addr):
    """
    Handles communication with a connected client.
    """
    print(f"Connected by {addr}")
    with conn:
        while True:

            data = conn.recv(1024)
            if not data:
                break

            print(f"Received: {data.decode('utf-8')}")

            conn.sendall(data)

def start_server(host='127.0.0.1', port=65432):

    print(f"Server is starting on {host}:{port}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

        server_socket.bind((host, port))

        server_socket.listen()
        print(f"Server is listening on {host}:{port}")

        while True:

            conn, addr = server_socket.accept()
            print(f"Connection accepted from {addr}")

            handle_client(conn, addr)

if __name__ == "__main__":
    start_server()
