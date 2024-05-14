from concurrent import futures
import time
from typing import OrderedDict
import uuid
from google.protobuf import wrappers_pb2

import grpc
import order_management_pb2_grpc
import order_management_pb2

class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer): 

    def __init__(self):
        self.orderDict = {}
        #Add a sample order 
        self.orderDict['101'] = order_management_pb2.Order(id='101', price=1000, 
                                                           items=['Item - A', 'Item - B'], 
                                                           description='Sample order description.')
        self.orderDict['102'] = order_management_pb2.Order(id='102', price=1000, 
                                                           items=['Item - C'], 
                                                           description='Sample order description.')
        self.orderDict['103'] = order_management_pb2.Order(id='103', price=1000, 
                                                           items=['Item - A', 'Item - E'], 
                                                           description='Sample order description.')
        self.orderDict['104'] = order_management_pb2.Order(id='104', price=1000, 
                                                           items=['Item - F', 'Item - G'], 
                                                           description='Sample order description.')                                                           

    # Unary RPC
    # метод getOrder принимает один запрос с ID заказа и возвращает один ответ, содержащий сообщение Order.
    # На вход в качестве запроса принимает один идентификатор заказа
    # он ищет этот заказ на стороне сервера и возвращает его в виде структуры типа Order.
    def getOrder(self, request, context):
        order = self.orderDict.get(request.value)
        if order is not None: 
            return order
        else: 
            # Error handling 
            print('Order not found ' + request.value)
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Order : ', request.value, ' Not Found.')
            return order_management_pb2.Order()

    # Unary RPC
    # Одиночный вызов. Принимает один запрос и возвращает один ответ. Метод добавляет заказ в словарь заказов.
    def addOrder(self, request, context):
        id = uuid.uuid1()
        request.id = str(id)
        self.orderDict[request.id] = request
        response = wrappers_pb2.StringValue(value=str(id))
        print(self.orderDict)
        return response

    # Server Streaming
    # В ответ на запрос сервер возвращает поток сообщений типа Order
    def searchOrders(self, request, context):  
        matching_orders = self.searchInventory(request.value)
        for order in matching_orders:
            yield order
    
    # Client Streaming
    # Принимает на входе поток данных и возвращает один ответ.
    def updateOrders(self, request_iterator, context):
        response = 'Updated IDs :'
        for order in request_iterator:
            self.orderDict[order.id] = order
            response += ' ' + order.id
        return wrappers_pb2.StringValue(value=response)

    #Bi-di Streaming
    # Сервер принимает поток данных и записывает эти данные в список. Сервер возрвращает этот список в виде потока сообщений типа Order.
    def processOrders(self, request_iterator, context):
        print('Processing orders.. ')
        shipment_id = uuid.uuid1() 
        shipments = []

        shipment = order_management_pb2.CombinedShipment(id=str(shipment_id), status='PROCESSED', )
        shipments.append(shipment)
        for order_id in request_iterator:
            for order in shipments:
                yield order

    # Local function
    # Принимает на вход запрос и возвращает список.
    def searchInventory(self, query):
        matchingOrders = []    
        for order_id, order in self.orderDict.items(): 
            for itm in order.items:
                if query in itm:
                    matchingOrders.append(order)
                    break
        return matchingOrders
 

# Creating gRPC Server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(), server)
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()



