import pika
import os


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


AMQP_URL = "<URL-OF-RABBITMQ-INSTANCE>"
url = os.environ.get('CLOUDAMQP_URL', AMQP_URL)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()


channel.queue_declare(queue='hello')

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()