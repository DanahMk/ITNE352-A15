## Project Title

# News Aggregator and Distribution Server

## Project Description

This project involves the development of a multi-threaded server application that aggregates news from various sources using the News API and distributes the fetched news data to connected clients upon request. The server listens for incoming client connections on a specified host and port, managing each client connection in a separate thread to handle multiple clients simultaneously

## Semester
Second Semester 2023/2024

## Group

- Group Name: - A15
- Course Code: ITNE352
- Section: 1
- Students Name: 
  1. Danah Mohammed Alkhan [202100476]
  2. Tayef Nabil Hassan Shehada [202101300]
  3. Hanan Nabeel Abdulla [202106695]
- Student ID:
  1. 202100476
  2. 202101300
  3. 202106695

## Table of Contents

1. [Requirements](#requirements)
2. [How to Run](#how-to-run)
3. [The Scripts](#the-scripts)
4. [Additional Concepts](#additional-concepts)
5. [Acknowledgments](#acknowledgments)
6. [Conclusion](#conclusion)
7. [Resources](#resources)

## Requirements

To set up and run this project locally, follow these steps:

### Prerequisites

- **Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **NewsAPI Key**: Sign up on [NewsAPI.org](https://newsapi.org/) to get your API key.

### Setup

1. **Clone the repository**
2. **Create a virtual environment**
3. **Activate the virtual environment**

## How to Run

### Start the Server: `python server.py`

### Run the Client: `python client.py `

Now, Enter your name when prompted and navigate through the menu options to search for news headlines or list sources.

## Scripts

### Server Script (server.py)

The server script retrieves news updates from NewsAPI.org and manages multiple client connections using multithreading. It handles different types of requests and sends the appropriate responses to the clients.

#### Main Functionalities:

Fetching news from NewsAPI based on different endpoints and parameters.
Handling multiple simultaneous client connections.
Sending JSON responses to clients.
Logging client connections and requests.

#### Utilized Packages:

socket for network communication.
threading for handling multiple clients.
requests for fetching news from NewsAPI.
json for processing JSON data.

### Client Script (client.py)

The client script presents a menu system to the user, allowing them to search for news headlines or list sources. It sends requests to the server and displays the results.

#### Main Functionalities:

Sending requests to the server based on user input.
Displaying news headlines and sources.
Navigating through a hierarchical menu system.

#### Utilized Packages:

socket for network communication.
json for processing JSON data.

## Additional Concepts
### Multithreading
The server uses multithreading to handle multiple clients simultaneously. This allows the server to manage several connections at once without blocking.

## Acknowledgments

Special thanks to our professor Dr. Mohammed Almeer for providing guidance and resources for this project.
Thanks to NewsAPI for providing the news data used in this project.
