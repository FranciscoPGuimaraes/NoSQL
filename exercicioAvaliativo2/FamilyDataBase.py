class FamilyDatabase:
    def __init__(self, database):
        self.db = database

    def get_parents(self):
        query = "match (p:Person)-[PARENT_OF]->(d:Person) return p"
        results = self.db.execute_query(query)
        return [result['p']['nome'] for result in results]

    def get_married(self):
        query = "MATCH p=()-[r:MARRIED_TO]->() RETURN p"
        results = self.db.execute_query(query)
        married_people = []

        for result in results:
            nodes = result['p'].nodes
            for node in nodes:
                if 'nome' in node:
                    married_people.append(node['nome'])

        return married_people

    def get_petsowner(self):
        query = "match (p:Person)-[OWNER]->(d:Animal) return p"
        results = self.db.execute_query(query)
        return [result['p']['nome'] for result in results]
