import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host, port))
while True:
    print(str(s.recv(1024), 'utf-8'))


