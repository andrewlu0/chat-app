# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import auth_pb2 as auth__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AuthStub(object):
    """Authentication interface
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Signup = channel.unary_unary(
                '/auth.Auth/Signup',
                request_serializer=auth__pb2.User.SerializeToString,
                response_deserializer=auth__pb2.Response.FromString,
                )
        self.Login = channel.unary_unary(
                '/auth.Auth/Login',
                request_serializer=auth__pb2.User.SerializeToString,
                response_deserializer=auth__pb2.Response.FromString,
                )
        self.SendChat = channel.unary_unary(
                '/auth.Auth/SendChat',
                request_serializer=auth__pb2.Chat.SerializeToString,
                response_deserializer=auth__pb2.Response.FromString,
                )
        self.GetChats = channel.unary_stream(
                '/auth.Auth/GetChats',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=auth__pb2.Chat.FromString,
                )


class AuthServicer(object):
    """Authentication interface
    """

    def Signup(self, request, context):
        """Signs up user and returns error if username already exists.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Logs in user and returns error if username doesn't exist or password is incorrect.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendChat(self, request, context):
        """Sends chat to server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChats(self, request, context):
        """Returns all chats in DB
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Signup': grpc.unary_unary_rpc_method_handler(
                    servicer.Signup,
                    request_deserializer=auth__pb2.User.FromString,
                    response_serializer=auth__pb2.Response.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=auth__pb2.User.FromString,
                    response_serializer=auth__pb2.Response.SerializeToString,
            ),
            'SendChat': grpc.unary_unary_rpc_method_handler(
                    servicer.SendChat,
                    request_deserializer=auth__pb2.Chat.FromString,
                    response_serializer=auth__pb2.Response.SerializeToString,
            ),
            'GetChats': grpc.unary_stream_rpc_method_handler(
                    servicer.GetChats,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=auth__pb2.Chat.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.Auth', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Auth(object):
    """Authentication interface
    """

    @staticmethod
    def Signup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/Signup',
            auth__pb2.User.SerializeToString,
            auth__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/Login',
            auth__pb2.User.SerializeToString,
            auth__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendChat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/SendChat',
            auth__pb2.Chat.SerializeToString,
            auth__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetChats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/auth.Auth/GetChats',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            auth__pb2.Chat.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
