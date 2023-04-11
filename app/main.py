# Uncomment this to pass the first stage
import socket
import re

def extract_words(s):
    matches = re.findall(r"\$\d+\r\n(.+?)\r\n", s)
    return matches

def is_ping(word):
    return word == b'PING'


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, _ = server_socket.accept() # wait for client

    data = b""

    is_RESP_array = False
    array_size = None
    last_counted_amount_of_words = 0


    while True:
        if is_RESP_array:
            current_list_of_words = extract_words(data)
            if len(current_list_of_words) > last_counted_amount_of_words:
                for word in current_list_of_words[last_counted_amount_of_words:]:
                    if is_ping(word):
                        conn.send(b"+PONG\r\n")
                    
            last_counted_amount_of_words = len(current_list_of_words)


        if b"*" in data and not is_RESP_array:
            is_RESP_array = True

        if is_RESP_array and not array_size and data.index(b"*") < len(data) - 1:
            array_size = data[data.index(b"*") + 1]

        
        chunk = conn.recv(256)
        print("chunk ", chunk)
        data += chunk

    










if __name__ == "__main__":
    main()
