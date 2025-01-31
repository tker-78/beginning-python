"""
説明:ネットワークプログラミングの自己学習のためのファイル
参考: https://docs.python.org/ja/3.13/howto/sockets.html

"""

import socket
import time

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print('waiting for connection: ', addr)
    c.send(bytes('successfully connected', 'utf-8'))
    num = 0
    for i in range(10):
        num += 1
        c.send(bytes(f'count: {num}', 'utf-8'))
        time.sleep(0.5)
    c.close()






