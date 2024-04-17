import argparse

from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://userweb21:567234@cluster0.vkwfwwg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.web21

parser = argparse.ArgumentParser(description="Cats Inc")
parser.add_argument("--action", help="create, update, read, delete")  # CRUD action
parser.add_argument("--id")
parser.add_argument("--name")
parser.add_argument("--age")
parser.add_argument("--features", nargs="+")

arg = vars(parser.parse_args())  # convert to dict

action = arg.get("action")
prime_key = arg.get("id")
name = arg.get("name")
age = arg.get("age")
features = arg.get("features")


def find():
    return db.cats.find()


def create(name, age, features):
    r = db.cats.insert_one(
        {
            "name": name,
            "age": age,
            "features": features,
        }
    )
    return r


def update(prime_key, name, age, features):
    r = db.cats.update_one(
        {"_id": ObjectId(prime_key)},
        {
            "$set": {
                "name": name,
                "age": age,
                "features": features,
            }
        },
    )
    return r


def delete(prime_key):
    return db.cats.delete_one({"_id": ObjectId(prime_key)})


def main():
    match action:
        case "create":
            r = create(name, age, features)
            print(r)
        case "read":
            r = find()
            print([e for e in r])
        case "update":
            r = update(prime_key, name, age, features)
            print(r)
        case "delete":
            r = delete(prime_key)
            print(r)
        case _:
            print("Unknown command")


if __name__ == "__main__":
    main()
