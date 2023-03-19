import pika


class RabbitMqServerConfigure(object):
    def __init__(self, host='localhost', queue='hello'):
        """Server initialization"""
        self.host = host
        self.queue = queue


class RabbitmqServer:
    def __init__(self, server):
        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._tem = self._channel.queue_declare(queue=self.server.queue)
        print('Server started waiting for Message')

    @staticmethod
    def callback(ch, method, properties, body):
        print(' [x] Received %r' % body)

    def strtserver(self):
        self._channel.basic_consume(queue=self.server.queue, on_message_callback=RabbitmqServer.callback, auto_ack=True)
        self._channel.start_consuming()


if __name__ == '__main__':
    serverconfigure = RabbitMqServerConfigure(host='localhost', queue='hello')
    server = RabbitmqServer(server=serverconfigure)
    server.strtserver()






# class MetaClass(type):
#     _instance = {}
#
#     def __call__(cls, *args, **kwargs):
#         """Singleton design pattern"""
#         if cls not in cls._instance:
#             cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
#             return cls._instance[cls]
