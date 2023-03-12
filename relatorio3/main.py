from database import Database
from helper.WriteAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
pokedex = Pokedex(db)

pokedex.getPokemonByName("Ivysaur")
pokedex.getPokemonsByType(["Grass", "Poison"])
pokedex.getFirePokemons()
pokedex.getFireWeaknessPokemons()
pokedex.getPokemonBySpawnChance()
