import socket
import json
import sys

LOG_FILE = "output.txt"

def rpc_valyrian_trans(sentence):
    HOST = '127.0.0.1'
    PORT = 65432
    
    # Package the request
    request = {
        "procedure": "valyrian_trans",
        "sentence": sentence
    }
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            
            # Send JSON
            s.sendall(json.dumps(request).encode('utf-8'))
            
            # Receive JSON
            response_bytes = s.recv(4096)
            response = json.loads(response_bytes.decode('utf-8'))
            
            if response.get("status") == "success":
                return response.get("result")
            else:
                return f"Error: {response.get('message')}"
                
    except ConnectionRefusedError:
        return "Error: Could not connect to server. Is it running?"

def main():
    print("--- Remote Valyrian Translator ---")
    while True:
        sent = input("\nWrite the words you want translated (or 'q' to quit): ")
        if sent.lower() == 'q':
            break
        
        with open(LOG_FILE, 'a') as f:
            f.write(f"User input:{sent}\n")
            translation = rpc_valyrian_trans(sent)
        
            print(f"Translation: {translation}")
            f.write(f"Translation:{translation}\n")

if __name__ == "__main__":
    main()