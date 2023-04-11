# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, _ = server_socket.accept() # wait for client

    data = b""

    while b"\r\n" not in data:
        chunk = conn.recv(256)
        print("chunk ", chunk)
        data += chunk

    conn.send(b"+PONG\r\n")










if __name__ == "__main__":
    main()
