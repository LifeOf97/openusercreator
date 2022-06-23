from pika.exchange_type import ExchangeType
from dotenv import load_dotenv
import pika
import os
import json

# Load env fil
load_dotenv()


class RabbitMQProducer:

    URL = os.environ.get('RABBITMQ_URL', 'amqp://guest:guest@localhost:5672')
    PARAMS = pika.URLParameters(URL)
    PARAMS.socket_timeout = 5
    EXCHANGE = ExchangeType.direct
    EXCHANGE_NAME = 'openuser'

    def __init__(self):
        self._connection = pika.BlockingConnection(parameters=self.PARAMS)
        self._channel = self._connection.channel()
        self._channel.exchange_declare(
            exchange=self.EXCHANGE_NAME,
            exchange_type=self.EXCHANGE,
            durable=True
        )

    def publish_new_creator(self, data, routing_key="new_creator"):
        """
        This method pushes message to our rabbitmq message broker exchange to be consumed
        by other microservices listening for messages with the specified routing_key.
        """
        self._channel.basic_publish(
            exchange=self.EXCHANGE_NAME,
            routing_key=str(routing_key),
            body=json.dumps(data),
            properties=pika.BasicProperties(content_type='application/json')
        )
        self._connection.close()

    def publish_create_openuserapp(self, data, routing_key='create_openuserapp'):
        """
        This method pushes message to our rabbitmq message broker exchange to be consumed
        by other microservices listening for messages with the specified routing_key.
        """
        self._channel.basic_publish(
            exchange=self.EXCHANGE_NAME,
            routing_key=str(routing_key),
            body=json.dumps(data),
            properties=pika.BasicProperties(content_type='application/json')
        )
        self._connection.close()
