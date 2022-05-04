from pymongo import MongoClient
def get_db_handle():
    client = pymongo.MongoClient('mongodb+srv://king20:kingshastri20@cluster0.ut1m1.mongodb.net/users?retryWrites=true&w=majority')

    db_handle = client['db_name']
    return db_handle


def get_collection_handle(db_handle, collection_name):
    return db_handle[collection_name]