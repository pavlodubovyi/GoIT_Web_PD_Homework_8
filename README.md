# MongoDB quotes database and email simulator

## Overview

This project is part of the GoIT Web Python course and demonstrates the use of MongoDB with MongoEngine ODM, JSON data processing, and message queuing with RabbitMQ. It consists of two main parts:

1. **Quote Management System**: Importing and querying quotes and authors from JSON files into a MongoDB database.
2. **Email Simulation System**: Simulating email sending using RabbitMQ with producer and consumer scripts.

---

## Part 1: Quote Management System

### Features

- **Data Import**: Parses `authors.json` and `quotes.json` files and imports the data into MongoDB collections (`authors` and `quotes`).
- **Data Modeling**: Utilizes MongoEngine to define `Author` and `Quote` models. The `Quote` model references the `Author` model using a `ReferenceField`.
- **Search Functionality**: Implements a command-line interface (`find_by_tags_authors.py`) that allows users to search for quotes by:
  - Author name: `name: Steve Martin`
  - Single tag: `tag: life`
  - Multiple tags: `tags: life,live`
- **UTF-8 Output**: Ensures all search results are displayed in UTF-8 format.

### Usage

1. **Setup MongoDB Atlas**: Create a cloud MongoDB database and obtain the connection URI.
2. **Configure Environment**: Update the MongoDB connection settings in your project.
3. **Install Dependencies**: Install required packages using Poetry:
   ```bash
   poetry install
   
## Part 2: Email Simulation System

### Features

- **Contact Model**: Defines a `Contact` model using MongoEngine with the following fields:
  - `full_name`: Full name of the contact.
  - `email`: Email address of the contact.
  - `is_sent`: Boolean field, default is `False`. Set to `True` once the message is "sent".
  - Additional fields can be added as needed for more context.
  
- **Producer Script (`producer.py`)**:
  - Generates a specified number of fake contacts using the `Faker` library.
  - Saves each contact into the MongoDB `contacts` collection.
  - Sends a message containing the ObjectID of each created contact to a RabbitMQ queue.
  
- **Consumer Script (`consumer.py`)**:
  - Listens to a RabbitMQ queue for incoming messages.
  - Each message contains the ObjectID of a contact.
  - Simulates sending an email to the contact using a placeholder function.
  - Updates the `is_sent` field to `True` in the database once the "email" has been sent.
  - Runs continuously, awaiting new messages.

### Usage

1. **Start RabbitMQ**: Ensure RabbitMQ is installed and running on your system or in the cloud.
2. **Configure Environment**: Make sure MongoDB and RabbitMQ connection settings are correctly set in your script (e.g., using a `.env` file).
3. **Run Producer**: Generate contacts and push messages to RabbitMQ queue:
   ```bash
   python producer.py
4. **Run Producer**  
   Generates fake contacts and pushes their ObjectIDs to the RabbitMQ queue.

   ```bash
   python producer.py
5. **Run Consumer**  
   This script listens to the RabbitMQ queue, processes messages by simulating email sending, and updates the `is_sent` field of the contact to `True`.

   ```bash
   python consumer.py

