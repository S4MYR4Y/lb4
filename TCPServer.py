import socket

def start_server(host='127.0.0.1', port=65432, buffer_size=4096):


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server up on {host}:{port}")

    while True:

        conn, addr = server_socket.accept()
        print(f"Connected з {addr}")


        file_name = conn.recv(buffer_size).decode()
        print(f"Rerieve file: {file_name}")


        with open(f"received_{file_name}", "wb") as file:
            while True:
                bytes_read = conn.recv(buffer_size)
                if not bytes_read:
                    break
                file.write(bytes_read)

        print(f"File {file_name} saved as як received_{file_name}")
        conn.close()
        print(f"Connection {addr} done\n")

if __name__ == "__main__":
    start_server()
