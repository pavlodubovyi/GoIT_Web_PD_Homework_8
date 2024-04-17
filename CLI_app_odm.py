import argparse

from bson.objectid import ObjectId
from mongoengine import connect, Document, StringField, IntField, ListField

connect(
    db="web21",
    host="mongodb+srv://userweb21:567234@cluster0.vkwfwwg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)

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


class Cat(Document):
    name = StringField(max_length=120, required=True)
    age = IntField(min_value=1, max_value=30)
    features = ListField(StringField(max_length=150))
    meta = {"collection": "cats"}


def find():
    return Cat.objects.all()


def create(name, age, features):
    r = Cat(name=name, age=age, features=features).save()
    return r


def update(prime_key, name, age, features):
    cat = Cat.objects(id=prime_key).first()  # None або кіт
    if cat:
        cat.update(name=name, age=age, features=features)
        cat.reload()
    return cat


def delete(prime_key):
    try:
        cat = Cat.objects.get(id=prime_key)  # якщо кота немає то помилка DoesNotExist
        cat.delete()
        return cat
    except DoesNotExist:
        return None


def main():
    match action:
        case "create":
            r = create(name, age, features)
            print(r.to_mongo().to_dict())
        case "read":
            r = find()
            print([e.to_mongo().to_dict() for e in r])
        case "update":
            r = update(prime_key, name, age, features)
            if r:
                print(r.to_mongo().to_dict())
            else:
                print("Not found")
        case "delete":
            r = delete(prime_key)
            if r:
                print(r.to_mongo().to_dict())
            else:
                print("Not found")
        case _:
            print("Unknown command")


if __name__ == "__main__":
    main()
