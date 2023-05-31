class teacherCRUD():

    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE(:Teacher{" + f"name:'{name}',ano_nasc:{ano_nasc},cpf:'{cpf}" + "'})"
        results = self.db.execute_query(query)
        return [results]

    def read(self, name):
        query = "MATCH(t:Teacher{name:'Chris Lima'}) RETURN t"
        results = self.db.execute_query(query)
        return [result["t"] for result in results]

    def update(self, name, cpf):
        query = "MATCH (t:Teacher{name:" + f"'{name}'" + "}) set t.cpf = " + f" '{cpf}'"
        results = self.db.execute_query(query)
        return [results]

    def delete(self, name):
        query = "MATCH (t:Teacher{name:" + f"'{name}'" + "}) DETACH DELETE t"
        results = self.db.execute_query(query)
        return [results]