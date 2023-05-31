class querys:
    def __init__(self, database):
        self.db = database

    def ex1query1(self):
        query = "MATCH (r:Teacher{name:'Renzo'}) return r.cpf, r.ano_nasc"
        results = self.db.execute_query(query)
        return [result for result in results]

    def ex1query2(self):
        query = "MATCH (r:Teacher) where r.name STARTS WITH 'M' return r.name, r.cpf"
        results = self.db.execute_query(query)
        return [result for result in results]

    def ex1query3(self):
        query = "MATCH (c:City) return c.name"
        results = self.db.execute_query(query)
        return [result for result in results]

    def ex1query4(self):
        query = "MATCH (s:School) where s.number>=150 and s.number<=550  return s.name, s.address, s.number"
        results = self.db.execute_query(query)
        return [result for result in results]

    def ex2query1(self):
        query = "MATCH (p:Teacher) RETURN p ORDER BY p.ano_nasc ASC LIMIT 1"
        results = self.db.execute_query(query)
        return [result for result in results]

    def ex2query2(self):
        query = "MATCH (p:Teacher) RETURN p ORDER BY p.ano_nasc DESC LIMIT 1"
        results = self.db.execute_query(query)
        return [result for result in results]

    def ex2query3(self):
        query = "MATCH (p:City) RETURN avg(p.population)"
        results = self.db.execute_query(query)
        return [result for result in results]

    def ex2query4(self):
        query = "MATCH (p:City{cep:'37540-000'}) RETURN replace(p.name, 'a', 'A')"
        results = self.db.execute_query(query)
        return [result for result in results]
