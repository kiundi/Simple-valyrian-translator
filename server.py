import socket
import json
import threading

def valyrain_trans(eng_sent):
    vowel_map = {'a': 'ar', 'e': 'el', 'i': 'ir', 'o': 'or', 'u': 'ul',
                 'A': 'Ar', 'E': 'El', 'I': 'Ir', 'O': 'Or', 'U': 'Ul'}

    working_sentence = eng_sent.lower()

    for original, valyrian in vowel_map.items():
        working_sentence = working_sentence.replace(original, valyrian)

    words = working_sentence.split()
    translated_sentence = ' '.join(words[::-1])

    if translated_sentence:
        translated_sentence = translated_sentence[0].upper() + translated_sentence[1:] + "-ys"
    
    return translated_sentence

def handle_client(conn, addr):
    print(f"Server: Connected by {addr}")
    try:
        # Receive data
        request_bytes = conn.recv(4096)
        if not request_bytes:
            return
        
        # Unpack JSON
        request_data = json.loads(request_bytes.decode('utf-8'))
        
        # Check if the client wants the "translate" procedure
        if request_data.get("procedure") == "valyrian_trans":
            sentence_to_process = request_data.get("sentence", "")
            
            result_text = valyrain_trans(sentence_to_process)
            
            response = {"status": "success", "result": result_text}
        else:
            response = {"status": "error", "message": "Unknown procedure"}

    except Exception as e:
        response = {"status": "error", "message": str(e)}
    finally:
        conn.sendall(json.dumps(response).encode('utf-8'))
        conn.close()

def start_server():
    HOST = '127.0.0.1'
    PORT = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server: Listening for sentences on {HOST}:{PORT}...")
        
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr))
            t.start()

if __name__ == "__main__":
    start_server()