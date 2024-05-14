import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('Старт сервера на {} порт {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    # ждем соединения
    print('Ожидание соединения...')
    connection, client_address = sock.accept()

    print('Подключено к:', client_address)
    # Принимаем данные порциями и ретранслируем их
    try:
        while True:
            data = connection.recv(64)
            if pickle.loads(data) == '':
                break
            print(f'Получено: {pickle.loads(data)}')
    except:
        pass
