# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
# from PySide6.QtNetwork import QTcpServer, QTcpSocket, QHostAddress
# from PySide6.QtGui import QPixmap
# import video_pb2  # Импортируем сгенерированный protobuf-класс
# import cv2
# import struct
#
#
# class VideoServer():
#     def __init__(self):
#         self.server = QTcpServer()
#         if not self.server.listen(address=QHostAddress.Any, port=5252):
#             print("Unable to start the server: %s." % self.server.errorString())
#         print('Server started')
#         self.message = video_pb2.Video()
#         self.window = QMainWindow()
#         self.window.setFixedSize(600, 600)
#         self.window.show()
#         self.server.newConnection.connect(self.new_connection)
#
#     def new_connection(self):
#         self.connection = self.server.nextPendingConnection()
#         self.connection.readyRead.connect(self.process_frame)
#         print(f'Connected to {self.connection}')
#
#     def process_frame(self):
#         # Десериализация protobuf-сообщения
#         data = bytes()
#         payload_size = struct.calcsize("q")
#         print("payload_size: {}".format(payload_size))
#         while len(data) < payload_size:
#             data += self.connection.readAll().data()
#         packed_msg_size = data[:payload_size]
#         data = data[payload_size:]
#         msg_size = struct.unpack("q", packed_msg_size)[0]
#         while len(data) < msg_size:
#             data += self.connection.readAll().data()
#         frame_data = data[:msg_size]
#         self.message.ParseFromString(frame_data)
#         print(len(self.message))
#         picture = QPixmap()
#         picture.loadFromData(self.message.video_data)
#         self.label.setPixmap(picture)
#         self.window.update()
#
#
#
#         # Получаем видео данные и выполняем необходимую обработкa
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     video_server = VideoServer()
#     sys.exit(app.exec())

import socket
import video_pb2   # Сгенерированный Protocol Buffers класс
import cv2
import numpy as np

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5252))
    server_socket.listen(1)
    print("Server started")
    conn, addr = server_socket.accept()

    frames_received = 0


    while True:
        # Получаем длину сообщения
        len_str = conn.recv(4)
        if not len_str:
            break

        # Получаем данные кадра
        msg_len = int.from_bytes(len_str, byteorder='big')
        frame_data = conn.recv(msg_len)
        print(len(frame_data))
        # Преобразуем данные в объект VideoFrame
        video_frame = video_pb2.Video()
        video_frame.ParseFromString(frame_data)

        frame = np.frombuffer(video_frame.frame_data, dtype=np.uint8)

        # Показываем кадр (или обрабатываем как хотим)
        frame = frame.reshape((480, 640, 3))
        cv2.imshow('Received Frame', frame)
        cv2.waitKey(1)

        frames_received += 1
        print(f"Received frame {frames_received}")

    server_socket.close()

if __name__ == '__main__':
    main()