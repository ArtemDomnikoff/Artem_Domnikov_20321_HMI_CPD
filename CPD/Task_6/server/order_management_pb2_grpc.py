# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from Artem_Domnikov_20321_HMI_CPD.CPD.Task_6.server import order_management_pb2 as Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


class OrderManagementStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.addOrder = channel.unary_unary(
                '/ecommerce.OrderManagement/addOrder',
                request_serializer=Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.Order.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                )
        self.getOrder = channel.unary_unary(
                '/ecommerce.OrderManagement/getOrder',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
                response_deserializer=Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.Order.FromString,
                )
        self.searchOrders = channel.unary_stream(
                '/ecommerce.OrderManagement/searchOrders',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
                response_deserializer=Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.Order.FromString,
                )
        self.updateOrders = channel.stream_unary(
                '/ecommerce.OrderManagement/updateOrders',
                request_serializer=Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.Order.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                )
        self.processOrders = channel.stream_stream(
                '/ecommerce.OrderManagement/processOrders',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
                response_deserializer=Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.CombinedShipment.FromString,
                )


class OrderManagementServicer(object):
    """Missing associated documentation comment in .proto file."""

    def addOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def searchOrders(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateOrders(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def processOrders(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrderManagementServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'addOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.addOrder,
                    request_deserializer=Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.Order.FromString,
                    response_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            ),
            'getOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.getOrder,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                    response_serializer=Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.Order.SerializeToString,
            ),
            'searchOrders': grpc.unary_stream_rpc_method_handler(
                    servicer.searchOrders,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                    response_serializer=Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.Order.SerializeToString,
            ),
            'updateOrders': grpc.stream_unary_rpc_method_handler(
                    servicer.updateOrders,
                    request_deserializer=Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.Order.FromString,
                    response_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            ),
            'processOrders': grpc.stream_stream_rpc_method_handler(
                    servicer.processOrders,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                    response_serializer=Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.CombinedShipment.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ecommerce.OrderManagement', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrderManagement(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def addOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecommerce.OrderManagement/addOrder',
            Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.Order.SerializeToString,
            google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecommerce.OrderManagement/getOrder',
            google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.Order.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def searchOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ecommerce.OrderManagement/searchOrders',
            google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.Order.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateOrders(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/ecommerce.OrderManagement/updateOrders',
            Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.Order.SerializeToString,
            google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def processOrders(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ecommerce.OrderManagement/processOrders',
            google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            Artem__Domnikov__20321__HMI__CPD_dot_CPD_dot_Task__6_dot_server_dot_order__management__pb2.CombinedShipment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
