import json
from datetime import datetime

import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

# channel.exchange_declare(exchange='Web_21_exchange', exchange_type='direct')
channel.queue_declare(queue='web_21_queue', durable=True)
# channel.queue_bind(exchange='Web_21_exchange', queue='web_21_queue')


def create_tasks(nums: int):
    for i in range(nums):
        message = {
            'id': i,
            'payload': f"Date: {datetime.now().date()}"
        }

        channel.basic_publish(exchange='Web_21_exchange', routing_key='web_21_queue', body=json.dumps(message).encode())

    connection.close()


if __name__ == '__main__':
    create_tasks(10)
