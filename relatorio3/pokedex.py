from database import Database
from helper.WriteAJson import writeAJson


class Pokedex():
    def __init__(self, database: Database):
        self._database = database

    def getPokemonsByType(self, types: list):
        pokemons = self._database.collection.find({"type": {"$in": types}})
        writeAJson(pokemons, "pokemons_by_type")

    def getPokemonByName(self, name: str):
        pokemons = self._database.collection.find({"name": name})
        writeAJson(pokemons, "pokemonByName")

    def getFirePokemons(self):
        pokemons = self._database.collection.find({"type": "Fire"})
        writeAJson(pokemons, "firePokemons")

    def getFireWeaknessPokemons(self):
        pokemons = self._database.collection.find({"weaknesses": "Fire"})
        writeAJson(pokemons, "fireWeaknessPokemons")

    def getPokemonBySpawnChance(self):
        pokemons = self._database.collection.find({"spawn_chance": {"$lt": 0.2}})
        writeAJson(pokemons, "pokemonBySpawnChance")
