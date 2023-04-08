from bson.objectid import ObjectId
from models.Motorista import Motorista


class MotoristaDAO:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_motorista(self, motorista: Motorista) -> str:
        try:
            result = self.collection.insert_one({"nome": motorista.nota,
                                                 "corridas": motorista.corridas})
            motorista_id = str(result.inserted_id)
            print(f"Motorista created with id: {motorista_id}")
            return motorista_id
        except Exception as error:
            print(f"An error occurred while creating an motorista: {error}")
            return None

    def read_motorista_by_id(self, motorista_id) -> dict:
        try:
            motorista = self.collection.find_one({"_id": ObjectId(motorista_id)})
            if motorista:
                print(f"Motorista found: {motorista}")
                return motorista
            else:
                print(f"No motorista found with id {motorista_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading an motorista: {error}")
            return None

    def update_motorista(self, motorista_id: str, motorista: Motorista) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(motorista_id)}, {"$set": {"nota": motorista.nota,
                                                                                           "corridas": motorista.corridas}})
            if result.modified_count:
                print(
                    f"Motorista {motorista_id} updated")
            else:
                print(f"No motorista found with id {motorista_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating an motorista: {error}")
            return None

    def delete_motorista(self, motorista_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(motorista_id)})
            if result.deleted_count:
                print(f"Motorista {motorista_id} deleted")
            else:
                print(f"No motorista found with id {motorista_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting an motorista: {error}")
            return None
