from app.mongo_db_operations import MongoDBOperation

mon=MongoDBOperation("user","user")

print(mon.get_collection("aws","Credentials"))