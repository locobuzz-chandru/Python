try:
    import pika
except Exception as e:
    print(f'some modules are missing {e}')


class MetaClass(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        """Singleton design pattern"""
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class RabbitMqConfigure(metaclass=MetaClass):
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


# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()
# channel.queue_declare(queue='hello')
# channel.basic_publish(exchange='', routing_key='hello', body='Hello World')
# print('Published Message')
# connection.close()
if __name__ == '__main__':
    server = RabbitMqConfigure(queue='hello', host='localhost', routingKey='hello', exchange='')
    with RabbitMq(server) as rabbitmq:
        rabbitmq.publish(payload={'Data': 22})
    # context manager-> automatically creates and closes the connection
