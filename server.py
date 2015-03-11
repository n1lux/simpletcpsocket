import socket
import sys

BUFFER_SIZE = 1024
MSG_FROM_SERVER = "Hello from server"

def create_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = 'localhost' 
    port = 8003


    sock.bind((host, port))
    sock.listen(10)

    print("Tcp server wait Conections on port 8003...")

    while True:
        try:
            (con, address) = sock.accept()
            print(address[0]+" Conected...")
            data = con.recv(BUFFER_SIZE)
            if len(str(data)) > 0:
                print(address[0]+" say: " + data.decode('UTF-8'))
                print("Response: " + MSG_FROM_SERVER)
                con.send(MSG_FROM_SERVER.encode('utf-8'))
            else:
                print("No data received from: "+address[0])
        except ValueError:
            print("Error: Accept")


if __name__== "__main__":
    create_server()
