import socket
from threading import Thread


def client_thread(conn, ip, port):
    is_active = True
    while is_active:
        client_input = conn.recv(1024).decode()
        if not client_input:
            break
        print("from connected user: " + str(client_input))
        if "bye" in client_input:
            print("Client is requesting to quit")
            conn.close()
            print("Connection " + ip + ":" + port + " closed")
            is_active = False
        else:
            data = input(' -> ')
            conn.send(data.encode())


def server_program():
    host = '10.153.3.191'
    port = 5557

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(2)

    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        Thread(target=client_thread, args=(conn, address[0], port)).start()
    server_socket.close()


if __name__ == '__main__':
    server_program()