import json
import pika
from faker import Faker
from models import Contact

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange="email", exchange_type="fanout")

fake = Faker("en_US")


def create_contact():
    # Generate fake contact data
    fullname = fake.name()
    email = fake.email()

    # Save contact to MongoDB
    contact = Contact(fullname=fullname, email=email)
    contact.save()

    # Publish contact data to RabbitMQ
    message = {"contact_id": str(contact.id)}
    channel.basic_publish(exchange="email", routing_key="", body=json.dumps(message).encode())
    print(f"Contact created: {contact.fullname} - {contact.email}")


if __name__ == '__main__':
    for _ in range(5):
        create_contact()
    connection.close()
