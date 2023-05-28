from database import Database
from FamilyDataBase import FamilyDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.202.189.58:7687", "neo4j", "mile-steels-helmet")

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
family_db = FamilyDatabase(db)

# Imprimindo todas as informações do banco de dados
opcao = int(input("""[1] - Quem da familia é pai/mãe?
[2] - Quem da familia é casado
[3] - Quem da familia é dono do pets
OPCÃO: """))
if opcao == 1:
    print("Parents:")
    print(family_db.get_parents())
elif opcao == 2:
    print("Couples:")
    print(family_db.get_married())
elif opcao == 3:
    print("Pets owners:")
    print(family_db.get_petsowner())

# Fechando a conexão com o banco de dados
db.close()