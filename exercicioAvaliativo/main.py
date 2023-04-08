from database import Database
from DAO.MotoristaDAO import MotoristaDAO

db = Database(database="Taxi", collection="Motorista")
db.resetDatabase()

taxi = MotoristaDAO(db)
