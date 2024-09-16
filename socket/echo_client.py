# Echo client program
import socket

def echo_client(server_host='127.0.0.1', server_port=4000):
    # Create a client scoket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        # Connect to the echo server
        client.connect((server_host, server_port))
        print(f'Connected to {server_host}:{server_port}')
        while True:
            # Input message
            message = input('Please input message(type "exit" to exit): ')
            if message.lower() == 'exit':
                break
            client.sendall(message.encode('utf-8'))
            # recv data
            data = client.recv(1024)
            print('received:', data.decode('utf-8'))


if __name__ == '__main__':
    echo_client()