# Uncomment this to pass the first stage
import socket
import re
import asyncio

def extract_redis_messages(s):
    print('extract')
    matches = re.findall(rb"\$\d+\r\n(.+?)\r\n", s)
    return matches

def is_ping(word):
    return word == b'ping'

def is_RESP_array(data):
    return b"*" in data

async def handle_redis_array(data: bytes, writer: asyncio.StreamWriter):
    messages = extract_redis_messages(data)
    for message in messages:
        if is_ping(message):
            writer.write(b"+PONG\r\n")

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    data = await reader.read(256)

    await asyncio.to_thread(handle_redis_array(data, writer))

    await writer.drain()

async def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    
    server = await asyncio.start_server(handle_client, "localhost", 6379)
    # conn, _ = server_socket.accept() # wait for client

    async with server:
        await server.serve_forever()

    # data = b""

    # while True:
    #     conn, _ = await server_socket.accept()

    #     if is_RESP_array(data):
    #         handle_redis_array(data)
    #         data = b""
        
    #     chunk = conn.recv(256)

    #     if not chunk:
    #         break

    #     data += chunk

    # conn.close()
    # server_socket.close()



if __name__ == "__main__":
    asyncio.run(main())
