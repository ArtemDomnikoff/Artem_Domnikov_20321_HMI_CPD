import cv2
import socket
import video_pb2
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Подключаем сокет к порту, через который прослушивается сервер
server_address = ('localhost', 5252)
print('Подключение к {} порт {}'.format(*server_address))

try:
    sock.connect(server_address)
    print('Подключено')
    vid = cv2.VideoCapture(0)
    message = video_pb2.Video()
    # Отправка данных
    while True:
        ret, frame = vid.read()
        cv2.imshow('client', frame)
        frame = cv2.resize(frame, (400, 400), interpolation=cv2.INTER_AREA)
        _, frame = cv2.imencode('.jpg', frame)
        string_data = frame.tobytes()
        # Заполняем protobuf-сообщение
        message.video_data = string_data

        # Отправляем данные на сервер
        serialized_message = message.SerializeToString()
        sock.sendall(struct.pack("l", len(serialized_message)) + serialized_message)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()

except ConnectionRefusedError:
    print('Подключение не установлено, сервер не отвечает')
except ConnectionResetError:
    pass




