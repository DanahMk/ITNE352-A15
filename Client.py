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

 if option == '1':
            keyword = input("Enter keyword: ")
            params = {'q': keyword}
            news_data = userRequest(client_socket, f'get_news|everything|{json.dumps(params)}')
            printResults(news_data)
        elif option == '2':
            category = input("Enter category (e.g., business, entertainment, general, health, science, sports, technology): ")
            params = {'category': category}
            news_data = userRequest(client_socket, f'get_news|top-headlines|{json.dumps(params)}')
            printResults(news_data)
 elif option == '3':
            country = input("Enter country code (e.g., us, in): ")
            params = {'country': country}
            news_data = userRequest(client_socket, f'get_news|top-headlines|{json.dumps(params)}')
            printResults(news_data)
        elif option == '4':
            news_data = userRequest(client_socket, 'get_news|top-headlines|{}')
            printResults(news_data)
        elif option == '5':
            break
        else:
            print("Invalid input. Please enter again.")

def fetchSources(client_socket):
    while True:
        print("List of sources menu:")
        print("1. Search by category")
        print("2. Search by country")
        print("3. Search by language")
        print("4. List all")
        print("5. Back to the main menu")
        option = input("Select an option: ")

