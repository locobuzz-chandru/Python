try:
    import pika
except Exception as e:
    print(f'some modules are missing {e}')


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

    @staticmethod
    def callback(ch, method, properties, body):
        print(' [x] Received %r' % body)

        with open('received.png', 'wb') as f:
            f.write(body)

    def strtserver(self):
        self._channel.basic_consume(queue=self.server.queue, on_message_callback=RabbitmqServer.callback, auto_ack=True)
        self._channel.start_consuming()


if __name__ == '__main__':
    serverconfigure = RabbitMqServerConfigure(host='localhost', queue='hello')
    server = RabbitmqServer(server=serverconfigure)
    server.strtserver()
