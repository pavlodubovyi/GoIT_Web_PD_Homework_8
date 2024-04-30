
import json
import os
import sys
import time

import pika
from models import Contact
from mongoengine import connect


def main():
    connect(db="PD_homework_8", host="mongodb+srv://userweb21:567234@cluster0.vkwfwwg.mongodb.net/")
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange="email", exchange_type="fanout")
    q = channel.queue_declare(queue='', exclusive=True)
    name_q = q.method.queue
    print(f"Random {name_q} queue created")
    channel.queue_bind(exchange="email", queue=name_q)

    def callback(ch, method, properties, body):
        message = json.loads(body.decode())
        process_message(message)

    channel.basic_consume(queue=name_q, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def process_message(message):
    contact_id = message.get('contact_id')
    contact = Contact.objects(id=contact_id).first()
    if contact:
        print(f"Sending email to {contact.email}...")
        # Simulating sending email
        time.sleep(0.5)
        print(f"Email sent to {contact.email}")
        # Mark contact as emailed
        contact.emailed = True
        contact.save()
    else:
        print(f"No contact with ID {contact_id} was found")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
