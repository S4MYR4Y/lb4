import threading
import socket

def test_client(host, port, message):

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            client_socket.sendall(message.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Response from server: {response}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 65432
    NUM_CLIENTS = 5

    threads = []

    for i in range(NUM_CLIENTS):
        message = f"Fianlly, it works, response client {i + 1}"
        client_thread = threading.Thread(target=test_client, args=(HOST, PORT, message))
        threads.append(client_thread)
        client_thread.start()

    for thread in threads:
        thread.join()
