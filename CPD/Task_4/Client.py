# import cv2
# import socket
# from PySide6.QtCore import *
# from PySide6.QtNetwork import *
# import video_pb2
# import struct
# import time
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # Подключаем сокет к порту, через который прослушивается сервер
# server_address = ('localhost', 5252)
# print('Подключение к {} порт {}'.format(*server_address))
#
# try:
#     sock.connect(server_address)
#     print('Подключено')
#     vid = cv2.VideoCapture(0)
#     message = video_pb2.Video()
#     # Отправка данных
#     while True:
#         # Отправка данных
#         ret, frame = vid.read()
#         _, img_encoded = cv2.imencode('.jpg', frame)
#         string_data = img_encoded.tobytes()
#
#         # Заполняем protobuf-сообщение
#         message.video_data = string_data
#
#         # Отправляем данные на сервер
#         serialized_message = message.SerializeToString()
#         print(len(serialized_message))
#         sock.sendall(struct.pack('q', len(serialized_message)) + serialized_message)
#         cv2.imshow('client', frame)
#         cv2.waitKey(1)
#
# except ConnectionRefusedError:
#     print('Подключение не установлено, сервер не отвечает')

import socket
import cv2
import video_pb2   # Сгенерированный Protocol Buffers класс

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5252))

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Создаем сообщение с кадром для отправки
        video_frame = video_pb2.Video(video_data=frame.tobytes())
        frame_data = video_frame.SerializeToString()

        # Отправляем данные серверу
        print(len(frame_data))
        client_socket.sendall(len(frame_data).to_bytes(4, byteorder='big'))
        client_socket.sendall(frame_data)
        # Add code for handling server response if needed

    cap.release()

if __name__ == '__main__':
    main()



