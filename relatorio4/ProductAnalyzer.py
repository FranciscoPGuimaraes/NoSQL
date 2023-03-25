from database import Database
from writeAJson import writeAJson

db = Database(database="mercado", collection="compras")


class ProductAnalyzer:

    def totalVendasDia(self):
        result = db.collection.aggregate([
            {
                "$group": {
                    "_id": "$data_compra",
                    "total": {
                        "$count": {}
                    }
                }
            }
        ])
        writeAJson(result, "Total de compras no dia")

    def produtoMaisVendido(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"}, {"$group": {"_id": "$produtos.descricao", "total": {"$count": {}}}}, {"$sort": {"total": -1}}, {"$limit": 1}
        ])
        writeAJson(result, "Produto mais vendido")

    def clienteMaisGastou(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"}, {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}, {"$sort": {"total": -1}}, {"$limit": 1}
        ])
        writeAJson(result, "Cliente que mais gastou")

    def produtosMaisDeUm(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"}, {"$group": {"_id": "$produtos.descricao", "total": {"$count": {}}}}
        ])
        writeAJson(result, "Produtos com mais de uma compra")
