import socket

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1) # only listening for 1 connection at a time
    c, addr = s.accept()
    print('Connection from: ' + str(addr))

    while True:
        data = c.recv(1024) # buffer with maximum of 1024 bytes
        if not data: # if connection is closed
            break
        print('from connected user: ' + str(data))
        data = str(data).upper()
        print('sending: ' + str(data))
        c.send(bytes(data, encoding='utf-8'))
    c.close()

if __name__ == '__main__':
    main()

