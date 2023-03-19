# RabbitMQ is a messaging broker, it gives our applications a common platform to send and receive messages, and our
# messages a safe place to live until received.
import pika


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

    def publish(self, payload={}):
        self._channel.basic_publish(exchange=self.server.exchange, routing_key=self.server.routingKey,
                                    body=str(payload))
        print(f'Published Message: {payload}')
        self._connection.close()


if __name__ == '__main__':
    server = RabbitMqConfigure(queue='hello', host='localhost', routingKey='hello', exchange='')
    rabbitmq = RabbitMq(server)
    rabbitmq.publish(payload={'Data': 22})
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()
# channel.queue_declare(queue='hello')
# channel.basic_publish(exchange='', routing_key='hello', body='Hello World')
# print('Published Message')
# connection.close()
