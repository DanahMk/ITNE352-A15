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
        
         if option == '1':
            category = input("Enter category (e.g., business, entertainment, general, health, science, sports, technology): ")
            params = {'category': category}
            sources_data = userRequest(client_socket, f'get_news|sources|{json.dumps(params)}')
            printSources(sources_data)
             
        elif option == '2':
            country = input("Enter country code (e.g., au, nz, ca, ae, sa, gb, us, eg, ma): ")
            params = {'country': country}
            sources_data = userRequest(client_socket, f'get_news|sources|{json.dumps(params)}')
            printSources(sources_data)
        elif option == '3':
            language = input("Enter language code (e.g., ar, en): ")
            params = {'language': language}
            sources_data = userRequest(client_socket, f'get_news|sources|{json.dumps(params)}')
            printSources(sources_data)
        elif option == '4':
            sources_data = userRequest(client_socket, 'get_news|sources|{}')
            printSources(sources_data)
        elif option == '5':
            break
        else:
            print("Invalid input. Please enter again.")

def printResults(news_data):
    if news_data['status'] == 'ok':
        for i, article in enumerate(news_data['articles']):
            print(f"{i+1}. {article['title']}")
        choice = int(input("Select an article number for details: "))
        if 1 <= choice <= len(news_data['articles']):
            article = news_data['articles'][choice-1]
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print(f"Source: {article['source']['name']}")
            print(f"URL: {article['url']}")
    else:
        print('Failed to fetch news.')

def printSources(sources_data):
    if sources_data['status'] == 'ok':
        for i, source in enumerate(sources_data['sources']):
            print(f"{i+1}. {source['name']} ({source['country']})")
    else:
        print('Failed to fetch sources.')

if __name__ == '__main__':
    client_name = input("Enter your name: ")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.send(client_name.encode('utf-8'))

    while True:
        print("Main menu:")
        print("1. Search headlines")
        print("2. List of sources")
        print("3. Quit")
        option = input("Select an option: ")

        if option == '1':
            fetchHeadlines(client_socket)
        elif option == '2':
            fetchSources(client_socket)
        elif option == '3':
            break
        else:
            print("Invalid input. Please enter again.")
    
    client_socket.close()

