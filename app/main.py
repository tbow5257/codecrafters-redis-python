# Uncomment this to pass the first stage
import socket
import re

def extract_words(s):
    print('extract')
    matches = re.findall(rb"\$\d+\r\n(.+?)\r\n", s)
    return matches

def is_ping(word):
    return word == b'ping'

def is_RESP_array(data):
    return data is not None and "*" in data


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, _ = server_socket.accept() # wait for client

    data = None

    array_size = None
    last_counted_amount_of_words = 0


    while True:
        print("top of true ", is_RESP_array(data))

        if data is not None and len(data) == 0:
            data = None
            continue

        if data is not None and is_RESP_array(data):
            print('enterrr')
            current_list_of_words = extract_words(data)

            for word in current_list_of_words:
                print(word)
                if is_ping(word):
                    conn.send(b"+PONG\r\n")
            
            data = None

        # if is_RESP_array and not array_size and data.index(b"*") < len(data) - 1:
        #     array_size = data[data.index(b"*") + 1]
        
        chunk = conn.recv(256)
        print("chunk ", chunk)
        data += chunk

    










if __name__ == "__main__":
    main()
