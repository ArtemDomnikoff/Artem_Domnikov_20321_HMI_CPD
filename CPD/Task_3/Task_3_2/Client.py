import socket
import time
import pickle

# СоздаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаем сокет к порту, через который прослушивается сервер
server_address = ('localhost', 10000)
print('Подключение к {} порт {}'.format(*server_address))
try:
    sock.connect(server_address)
    print('Подключено')

    while True:
        # Отправка данных
        message = pickle.dumps('Hello World')
        sock.send(message)
        time.sleep(1)

except ConnectionRefusedError:
    print('Подключение не установлено, сервер не отвечает')

except:
    pass



