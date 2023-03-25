from database import Database
from ProductAnalyzer import ProductAnalyzer
from writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
#db.resetDatabase()

analizador = ProductAnalyzer()
analizador.totalVendasDia()
analizador.produtoMaisVendido()
analizador.clienteMaisGastou()
analizador.produtosMaisDeUm()


