try:
    import pika
except Exception as e:
    print(f'some modules are missing {e}')


class RabbitMqConfigure(object):
    """Configure RabbitMq Server"""

    def __init__(self, queue='hello', host='localhost', routingKey='hello', exchange=''):
        self.queue = queue
        self.host = host
        self.routingKey = routingKey
        self.exchange = exchange


class RabbitMq(object):
    def __init__(self, server):
        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        self._connection.close()

    def publish(self, payload={}):
        self._channel.basic_publish(exchange=self.server.exchange, routing_key=self.server.routingKey,
                                    body=str(payload))
        print(f'Published Message: {payload}')


class Image(object):
    def __init__(self, filename):
        self.filename = filename

    @property
    def get(self):
        with open(self.filename, 'rb') as f:
            data = f.read()
        return data


if __name__ == '__main__':
    server = RabbitMqConfigure(queue='hello', host='localhost', routingKey='hello', exchange='')
    image = Image(filename='E:\Projects\Python\RabbitMq\image.png')
    data = image.get
    with RabbitMq(server) as rabbitmq:
        rabbitmq.publish(payload=data)
    # context manager-> automatically creates and closes the connection
