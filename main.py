from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://userweb21:567234@cluster0.vkwfwwg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.web21

try:
    db.cats.insert_many(
        [
            {
                "name": "Boris",
                "age": 12,
                "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
            },
            {
                "name": "Murzik",
                "age": 1,
                "features": ["ходить в лоток", "дає себе гладити", "чорний"],
            },
        ]
    )
except Exception as e:
    print(e)
