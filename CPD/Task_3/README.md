## ВзаимодействиеКлиент-Сервер
### Клиент-Сервер через Сокеты
## Листинг 1_1 Client
```Py
import time

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
        message = 'Hello World'.encode()
        sock.send(message)
        time.sleep(1)

except ConnectionRefusedError:
    print('Подключение не установлено, сервер не отвечает')

except:
    pass
```
## Листинг 1_2 Server
```Py
import socket

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
            if data.decode() == '':
                break
            print(f'Получено: {data.decode()}')
    except:
        pass
```
### Клиент-Сервер с pickle
## Листинг 2_1 Client
```Py
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

```

## Листинг 2_2 Server
```Py
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
```
### Клиент-Сервер через protobuf
## Листинг 3_1 Client
```Py
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
```
## Листинг 3_2 Server
```Py
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
```