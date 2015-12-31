import socket

def main():
    host = '127.0.0.1'
    port = 5001

    server = (host, 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input('->')
    while message != 'EXIT':
        s.sendto(bytes(message, encoding='utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('Received from server:' + data)
        message = input('->')
    s.close()

if __name__ == '__main__':
    main()

