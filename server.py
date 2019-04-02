import socket


def server_program():
    host = '10.153.3.191'
    port = 7734

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen()
    conn, address = server_socket.accept()

    print("Connection from: " + str(address))

    while 1:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    server_program()