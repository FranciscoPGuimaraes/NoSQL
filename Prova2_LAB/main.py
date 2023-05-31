from database import Database
from query import querys
from teacher_crud import teacherCRUD


# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.216.125.197:7687", "neo4j", "disadvantages-offense-leak")

# Criando uma instância da classe teacherDatabase e query para interagir com o banco de dados
teacherDB = teacherCRUD(db)
query = querys(db)

# CRUD
teacherDB.create("Chris Lima", 1956, "189.052.396-66")
teacher = teacherDB.read("Chris Lima")
print(teacher)
teacherDB.update("Chris Lima", "162.052.777-77")
teacher = teacherDB.read("Chris Lima")
print(teacher)

# Imprimindo todas as informações do banco de dados
op = int(input("""
[1] Exercicio 1:
    a) 11
    b) 12
    c) 13
    d) 14
[2] Exercicio 2:
    a) 21
    b) 22
    c) 23
    d) 24
    
    Opção: """))
if op == 11:
    q = query.ex1query1()
elif op == 12:
    q = query.ex1query2()
elif op == 13:
    q = query.ex1query3()
elif op == 14:
    q = query.ex1query4()
elif op == 21:
    q = query.ex2query1()
elif op == 22:
    q = query.ex2query2()
elif op == 23:
    q = query.ex2query3()
elif op == 24:
    q = query.ex2query4()
else:
    q = "Opção invalida"
print(q)

# Fechando a conexão com o banco de dados
db.close()