import socket
import json

HOST = '127.0.0.1'
PORT = 65432
def userRequest(client_socket, request):
    client_socket.send(request.encode('utf-8'))
    response_length_str = client_socket.recv(10).decode('utf-8').strip()
    print(f"Received response length string: '{response_length_str}'")
    response_length = int(response_length_str)
    print(f"Received response length: {response_length}")
    response_data = b""
    while len(response_data) < response_length:
        part = client_socket.recv(response_length - len(response_data))
        response_data += part

    return json.loads(response_data.decode('utf-8'))
    def fetchHeadlines(client_socket):
    while True:
        print("Search headlines menu:")
        print("1. Search for keywords")
        print("2. Search by category")
        print("3. Search by country")
        print("4. List all new headlines")
        print("5. Back to the main menu")
        option = input("Select an option: ")
