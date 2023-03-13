from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
  def __init__(self, db: Database):
    self.db = db

  def listAll(self):
    pokemons = self.db.collection.find()
    writeAJson(pokemons, "pokemons")

  def getPikachu(self):
    pikachu = self.db.collection.find({"name": "pikachu"})
    writeAJson(pikachu, "pokemons") 

  def getPoisonPokemons(self):
    poisonPokemons = self.db.collection.find({"type": {"$in": ["Poison"]}})
    writeAJson(poisonPokemons, "poisonPokemons") 

  def getPokemonsWeakAgainstFire(self):
    pokemonsWeakAgainstFire = self.db.collection.find({"weaknesses": {"$all": ["Fire"]}})
    writeAJson(pokemonsWeakAgainstFire, "pokemonsWeakAgainstFire")
  
  def getPokemonsBySpawnChance(self):
    pokemonsBySpawnChance = self.db.collection.find({"spawn_chance": {"$gt": 0.4, "$lt": 0.8}})
    writeAJson(pokemonsBySpawnChance, "pokemonsBySpawnChance")