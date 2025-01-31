from mysocket import MySocket
import socket

s = MySocket()
s.sock.bind((s.host, s.port))
s.sock.listen(5)

while True:
    c, address = s.sock.accept()
    s.mysend(bytes('hello, socket.', 'utf-8'))

