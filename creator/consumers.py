from pika.exchange_type import ExchangeType
from pika.channel import Channel
from celery import Celery
import pika
import os
import json


URL = os.environ.get('RABBITMQ_URL')
PARAMS = pika.URLParameters(URL)
PARAMS.socket_timeout = 5
EXCHANGE = ExchangeType.direct
EXCHANGE_NAME = 'openuser'
DEFAULT_QUEUE_NAME = 'open_user_data'
OPENUSERAPP_KEY = 'update_openuserapp'

# Connect to main Celery instance
celery_app = Celery('src', broker=os.environ.get('REDIS_URL'))


def main():
    connection = pika.BlockingConnection(parameters=PARAMS)
    channel = connection.channel()
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type=EXCHANGE, durable=True)

    def callback(ch: Channel, mth, props, body):
        if mth.routing_key == OPENUSERAPP_KEY:
            print(F"Recieved ({mth.routing_key}) message: {json.loads(body)}")
            celery_app.send_task(name='creator.tasks.update_openuserapp', kwargs={'data': json.loads(body)})

        # Always acknowledge message delivery
        ch.basic_ack(delivery_tag=mth.delivery_tag)

    # declare queue
    openuserdata_queue = channel.queue_declare(queue=DEFAULT_QUEUE_NAME, durable=True)

    # bind queue to exchange and consume messages with OPENUSERAPP_KEY routing_key
    channel.queue_bind(queue=openuserdata_queue.method.queue, exchange=EXCHANGE_NAME, routing_key=OPENUSERAPP_KEY)
    channel.basic_consume(queue=openuserdata_queue.method.queue, on_message_callback=callback)

    print(F"Waiting for ({OPENUSERAPP_KEY}) messages in ({openuserdata_queue.method.queue}) queue")

    channel.start_consuming()
    connection.close()


if __name__ == '__main__':
    main()
