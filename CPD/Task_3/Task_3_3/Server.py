import socket
import data_pb2

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)
print('Сервер запущен на {} порт {}'.format(*server_address))
while True:
    # ждем соединения
    print('Ожидание соединения...')
    connection, client_address = sock.accept()

    print('Подключено к:', client_address)
    # Принимаем данные порциями и ретранслируем их
    try:
        while True:
            recieved_data = connection.recv(64)
            data = data_pb2.Data()
            data.ParseFromString(recieved_data)
            if data == '':
                break
            print(f'Получено: {data.device_id, data.event_id}')
    except:
        pass
