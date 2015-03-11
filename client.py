import socket
import sys

server = 'localhost'
port = 8003
buffer_size = 1024 
MSG = "Hello word"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((server, port))
    print("To send >>>"+ MSG)
    sock.send(MSG.encode('utf-8'))
    data = sock.recv(buffer_size)
    if len(str(data)) > 0:
        print("Receiv from server: "+data.decode('utf-8'))
    else:
        print("No data received from server...")
except ValueError:
    print("Erro connect!")

