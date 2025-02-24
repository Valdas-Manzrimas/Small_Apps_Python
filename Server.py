import socket 
from threading import Thread #Allows multiple threads to run at the same time

host='localhost'
port=8080

clients={}
addresses={}

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # SOCK_STREAM = TCP ; SOCK_DGRAM = UDP
sock.bind((host,port))

def accept_clients_connections(): 
    while True:
        client_conn,client_address=sock.accept()
        print(client_address, 'Has connected')
        client_conn.send('Welcome to the chat'.encode('utf-8'))
        addresses[client_conn]=client_address

if __name__ == "__main__":
    sock.listen(5)
    print("Server is running")

    t1=Thread(target=accept_clients_connections)
    t1.start()
    t1.join() #Waits for the thread to finish