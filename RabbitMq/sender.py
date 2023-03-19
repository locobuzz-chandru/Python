try:
    import pika
except Exception as e:
    print(f'some modules are missing {e}')


class RabbitMq(object):
    def __init__(self, queue='hello'):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self._channel = self._connection.channel()
        self.queue = queue
        self._channel.queue_declare(queue=self.queue)

    def publish(self, payload={}):
        self._channel.basic_publish(exchange='', routing_key='hello', body=str(payload))
        print('Published....')
        self._connection.close()


# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()
# channel.queue_declare(queue='hello')
# channel.basic_publish(exchange='', routing_key='hello', body='Hello World')
# print('Published Message')
# connection.close()
if __name__ == '__main__':
    server = RabbitMq(queue='hello')
    server.publish(payload={'Data': 'hello'})
