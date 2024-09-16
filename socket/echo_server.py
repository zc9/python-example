# Echo server program
import socket
def echo_server(host='127.0.0.1', port=4000):

    # Create a server socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # bind
        server.bind((host, port))
        # listen
        server.listen()
        print(f'The echo server has started, listening at {host}:{port}')
        while True:
            # Accept a new connection
            client, addr = server.accept()
            print(f'The new connection is from {addr}')
            while True:
                # recv
                data = client.recv(1024)
                if not data:
                    print(f'Disconnect from {addr}')
                    break
                print('received:', data.decode('utf-8'))
                client.sendall(data)

if __name__ == '__main__':
    echo_server()