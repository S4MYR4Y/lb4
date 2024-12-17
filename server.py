import socket

def start_server(host='127.0.0.1', port=65432):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

            server_socket.bind((host, port))
            server_socket.listen()
            print(f"Server works on {host}:{port}...")

            while True:

                conn, addr = server_socket.accept()
                print(f"Connected {addr}")


                with conn:
                    while True:

                        data = conn.recv(1024)
                        if not data:
                            print(f"Client {addr} disconnected")
                            break

                        print(f"REcieved from  {addr}: {data.decode('utf-8')}")

                        conn.sendall(data)


if __name__ == "__main__":
    start_server()
