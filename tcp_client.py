import socket

def main():
    host = '127.0.0.1'
    try:
        settings = open('./settings.txt', 'r').readlines()
        if len(settings) > 0:
            host = settings[0]
    except Exception as e:
        print(str(e))
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    message = input('->')
    while message != 'EXIT':
        s.send(bytes(message, encoding='utf-8'))
        data = s.recv(1024) # buffer of 1024
        print('Received from server: ' + data.decode('utf-8'))
        message = input('->')
    s.close()

if __name__ == '__main__':
    main()

