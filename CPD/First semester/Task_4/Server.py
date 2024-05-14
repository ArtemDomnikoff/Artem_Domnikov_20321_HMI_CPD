import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtNetwork import QTcpServer, QHostAddress
import video_pb2
import numpy as np
import cv2
import struct


class VideoServer:
    def __init__(self):
        self.server = QTcpServer()
        if not self.server.listen(address=QHostAddress.Any, port=5252):
            print("Unable to start the server: %s." % self.server.errorString())
        print('Server started')
        self.message = video_pb2.Video()
        self.server.newConnection.connect(self.new_connection)

    def new_connection(self):
        self.connection = self.server.nextPendingConnection()
        self.connection.readyRead.connect(self.process_frame)
        print(f'Connected to {self.connection}')

    def process_frame(self):
        try:
            # Десериализация protobuf-сообщения
            data = b''
            payload_size = struct.calcsize("l")
            while len(data) < payload_size:
                data += self.connection.read(4).data()
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("l", packed_msg_size)[0]
            data += self.connection.readAll().data()
            frame_data = data[:msg_size]
            self.message.ParseFromString(frame_data)
            frame = np.frombuffer(self.message.video_data, dtype=np.byte)
            frame = cv2.imdecode(frame, cv2.IMREAD_UNCHANGED)
            frame = cv2.resize(frame, (800, 600), interpolation=cv2.INTER_AREA)
            cv2.imshow('server', frame)
            cv2.waitKey(1)
        except:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    video_server = VideoServer()
    sys.exit(app.exec())


