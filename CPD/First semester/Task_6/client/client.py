from google.protobuf import wrappers_pb2
import grpc
import order_management_pb2
import order_management_pb2_grpc

import time


def run():
    # Подключение к серверу на порт 50051
    channel = grpc.insecure_channel('localhost:50051')

    # Создаётм объект класса OrderManagementStub
    stub = order_management_pb2_grpc.OrderManagementStub(channel)

    # Создаём объект класса Order и задаём его атрибуты.
    order1 = order_management_pb2.Order(items=['Item - A', 'Item - B', 'Item - C'],
                                        price=2450.50,
                                        description='This is a Sample order - 1 : description.',
                                        destination='San Jose, CA')

    # Вызываем метод getOrder и передаём в качестве аргумента экземпляр класса Order
    order = stub.getOrder(order_management_pb2.Order(id='101'))
    print("Order service response", order)

    # Unary RPC : Adding an Order
    # Добавляем заказ в словарь на сервере.
    response = stub.addOrder(order1)
    print('Add order response :', response)

    # Server Streaming
    # Сервер возвращает поток данных в ответ на запрос.
    for order_search_result in stub.searchOrders(wrappers_pb2.StringValue(value='Item - A')):
        print('Search Result : ', order_search_result)

    # Client Streaming
    # Клиент передаёт поток данных на сервер, сервер возвращает одно значение.
    upd_order_iterator = generate_orders_for_updates()
    upd_status = stub.updateOrders(upd_order_iterator)
    print('Order update status : ', upd_status)

    # Bi-di Streaming
    # Клиент передаёт поток данных на сервер и в ответ принимает поток данных.
    proc_order_iterator = generate_orders_for_processing()
    for shipment in stub.processOrders(proc_order_iterator):
        print(shipment)

# Генерирует заказы и добавляет их в список. Возвращает список как генератор.
def generate_orders_for_updates():
    ord1 = order_management_pb2.Order(id='101', price=1000,
                                      items=['Item - A', 'Item - B', 'Item - C', 'Item - D'],
                                      description='Sample order description.',
                                      destination='Mountain View, CA')
    ord2 = order_management_pb2.Order(id='102', price=1000,
                                      items=['Item - E', 'Item - Q', 'Item - R', 'Item - D'],
                                      description='Sample order description.',
                                      destination='San Jose, CA')
    ord3 = order_management_pb2.Order(id='103', price=1000,
                                      items=['Item - A', 'Item - K'],
                                      description='Sample order description.',
                                      destination='San Francisco, CA')
    list = []
    list.append(ord1)
    list.append(ord2)
    list.append(ord3)

    for updated_orders in list:
        yield updated_orders

 # Генерирует заказы и добавляет их в список. Возвращает список как генератор.
def generate_orders_for_processing():
    ord1 = order_management_pb2.Order(
        id='104', price=2332,
        items=['Item - A', 'Item - B'],
        description='Updated desc',
        destination='San Jose, CA')
    ord2 = order_management_pb2.Order(
        id='105', price=3000,
        description='Updated desc',
        destination='San Francisco, CA')
    ord3 = order_management_pb2.Order(
        id='106', price=2560,
        description='Updated desc',
        destination='San Francisco, CA')
    ord4 = order_management_pb2.Order(
        id='107', price=2560,
        description='Updated desc',
        destination='Mountain View, CA')
    list = []
    list.append(ord1)
    list.append(ord1)
    list.append(ord3)
    list.append(ord4)

    for processing_orders in list:
        yield processing_orders


run()
