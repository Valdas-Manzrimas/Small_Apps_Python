import socket 
from threading import Thread #Allows multiple threads to run at the same time

host='localhost'
port=8080

clients={}
addresses={}

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # SOCK_STREAM = TCP ; SOCK_DGRAM = UDP
sock.bind((host,port))

def handle_clients(conn,address):
    try:
        name=conn.recv(1024).decode('utf-8')
        welcome =  'Welcome '+name+'! if you want to quit this chat, type #quit'
        conn.send(bytes(welcome,'utf-8'))
        msg = name + ' has joined the chat'
        broadcast(bytes(msg,'utf-8'))
        clients[conn]=name

        while True:
            msg = conn.recv(1024)
            if not msg:
                    break
            if msg != bytes('#quit','utf-8'):
                broadcast(msg,name + ": ")
            else:
                break
    except Exception as e:
        print(f"Error handling client {name}: {e}")
    finally:
        conn.close()
        del clients[conn]
        print(address, 'Has disconnected')
        broadcast(bytes(name + ' has left the chat', 'utf-8'))
            

def accept_clients_connections(): 
    while True:
        client_conn,client_address=sock.accept()
        print(client_address, 'Has connected')
        client_conn.send('Welcome to the chat, please type your name to continue'.encode('utf-8'))
        addresses[client_conn]=client_address

        Thread(target=handle_clients,args=(client_conn,client_address)).start()

def broadcast(msg,prefix=""):
    for sock in list(clients.keys()):
        try:
            sock.send(bytes(prefix, 'utf-8') + msg)
        except Exception as e:
            print(f"Error broadcasting to {clients[sock]}: {e}")
            sock.close()
            del clients[sock]


if __name__ == "__main__":
    sock.listen(5)
    print("Server is running")

    t1=Thread(target=accept_clients_connections)
    t1.start()
    t1.join() #Waits for the thread to finish