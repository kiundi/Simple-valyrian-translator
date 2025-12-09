# Remote Valyrian Translator

A Python-based Remote Procedure Call (RPC) system that translates English sentences into pseudo-High Valyrian. This project demonstrates the implementation of a client-server architecture using raw sockets, JSON serialization, and multi-threading.

# 📋 Overview
The application is split into two parts:

Server: Hosts the translation logic and listens for incoming TCP connections. It handles multiple clients simultaneously using threading.

Client: Accepts user input, packages the request into JSON, sends it to the server, and logs the results to a file.

# ⚙️ Features
Custom RPC Protocol: Implements a request-response pattern using JSON over TCP sockets.

Concurrency: The server uses threading to handle multiple client connections at once.

Data Marshaling: Uses json to serialize and deserialize data between the client and server.

Logging: Client interactions are automatically saved to output.txt.

Translation Algorithm: Performs vowel mapping, syntax inversion, and suffix modification.

# 🚀 Usage
Prerequisites
Python 3.x

## 1. Start the Server
Run the server script first. It will bind to 127.0.0.1:65432 and wait for connections.

Bash

python server.py
## 2. Start the Client
Open a new terminal window and run the client script.

Bash

python client.py
## 3. Translate
Enter sentences when prompted. Type q to exit.

## Example Interaction:

Plaintext

Write the words you want translated (or 'q' to quit): hello world

## Translation: World hellor-ys
📂 Project Structure
server.py: Contains the RPC stub, connection listener, and the valyrain_trans logic.

client.py: The user interface that connects to the server and logs output.

output.txt: Created automatically to store a history of inputs and translations.

## 🧠 Translation Logic
The "Valyrian" conversion follows these steps:

Vowel Expansion: Vowels are mapped to longer sounds (e.g., 'a' → 'ar', 'o' → 'or').

Syntax Inversion: The word order of the sentence is reversed.

Suffixing: The sentence is capitalized and ends with -ys.