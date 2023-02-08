import pymongo
import os

CONNECTION_STRING = str(os.getenv("CONNECTION_STRING"))
DATABASE_NAME = str(os.getenv("DATABASE_NAME"))
COL_NAME = str(os.getenv("COL_NAME"))


class MongodbRepository:
    def __init__(self) -> None:
        self.connection = None
        self.db = None

        self.connect()
        self.get_mongo_db()

    def connect(self):
        try:
            self.connection = pymongo.MongoClient(CONNECTION_STRING)
        except:
            raise

    def get_mongo_db(self):
        self.db = self.connection[DATABASE_NAME]

    def get_collection(self, name=COL_NAME):
        return self.db[COL_NAME]

    def find_all_items(self, collection):
        """
        Execute SELECT * FROM mycollection
        """
        all_documents = collection.find({})

        return all_documents

    def count_all_items(self, collection, _filter={}):
        """
        Execute SELECT * FROM mycollection
        """
        all_documents = collection.count_documents(_filter)

        return all_documents
    
    def find_by_x_embbeded(self, collection):
        """
        SELECT * FROM mycollection WHERE <field> = <value>
        """
        return collection.find(
            {
                "x.origin": {"$eq": "value1"},
                "y.destination": {"$eq": "value2"},
            }
        )
