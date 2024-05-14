import socket
import time
import data_pb2

# СоздаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаем сокет к порту, через который прослушивается сервер
server_address = ('localhost', 10000)
print('Подключение к {} порт {}'.format(*server_address))
try:
    sock.connect(server_address)
    print('Подключено')

    while True:
        data = data_pb2.Data()
        data.device_id = 1000
        data.event_id = 2
        # Отправка данных
        serealized_data = data.SerializeToString()
        sock.sendall(serealized_data)
        time.sleep(1)

except ConnectionRefusedError:
    print('Подключение не установлено, сервер не отвечает')




