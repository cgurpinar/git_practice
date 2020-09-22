import random
pokemon_type_lists = {
  "Fire":{
    "Fire": 1 / 2,
    "Water": 1 / 2,
    "Grass": 2
  },
  "Water":{
    "Fire": 2,
    "Water": 1 / 2,
    "Grass": 1 / 2
  },
  "Grass":{
    "Fire": 1 / 2,
    "Water": 2,
    "Grass": 1 /2
  }
}

class Pokemon:
  is_knocked_out = False

  def __init__(self, name, level, pokemon_type):
    self.name = name
    self.level = level
    self.pokemon_type = pokemon_type
    self.max_health = level
    self.exp = 2
    self.speed = level

  def lose_health(self, damage):
    self.max_health -= damage
    if self.max_health <= 0:
      self.max_health = 0
      self.knocked_out()
    else:
      print("{} has {} health.".format(self.name, self.max_health))
  
  def knocked_out(self):
    print("{} knocked out.".format(self.name))
    self.is_knocked_out = True
    self.revive()

  def revive(self):
    self.max_health = 1
    self.is_knocked_out = False
    print("{} was riveved with {} health".format(self.name, self.max_health))

  def attack(self, other):
    if self.is_knocked_out == False or self.max_health != 1:
      if self.pokemon_type in pokemon_type_lists:
        if other.pokemon_type in pokemon_type_lists[self.pokemon_type]:
          multiplier = pokemon_type_lists[self.pokemon_type][other.pokemon_type]
          print("{} ({} type pokemon), attack {} ({} type pokemons).".format(self.name, self.pokemon_type, other.name, other.pokemon_type))
          if multiplier == 2:
            print("{} very effective against {} type pokemons.".format(self.name, other.pokemon_type))
          else:
            print("{} not effective against {} type pokemons.".format(self.name, other.pokemon_type))
          damage = self.level * multiplier
          print("{} taken {} damage.".format(other.name, damage))
          other.lose_health(damage)
          self.gain_exp(1)
        else:
          return "Pokemon type out of range"
      else:
        return "Pokemon type out of range"
    else:
      print("{} just knocked out/revived switch your pokemon".format(self.name))

  def restore_health(self, health):
    self.health = health
    if self.is_knocked_out == True:
      self.revive()
    else:
      self.max_health += self.health
      if self.max_health > self.level:
        self.max_health = self.level
        print("{} gained {} health. Now health: {}".format(self.name,self.health, self.max_health))
      else:
        print("{} gained {} health. Now health: {}".format(self.name, self.health, self.max_health))

  def gain_exp(self, exp):
    self.exp += exp
    print("{} gained {} exp.".format(self.name, exp))
    self.level_up()

  def level_up(self):
    if self.exp > 2:
      self.level += 1
      self.maximum_health = self.level
      print("{} level up. Now: {} level, {} hp".format(self.name, self.level, self.maximum_health))
      self.evolve()

  def evolve(self):
    if self.level == 10:
      evolved_name = "Mega " + self.name
      print("{} has evolved. Evolved to: {}".format(self.name, evolved_name))
      self.name = evolved_name


class Trainer:
  def __init__(self, name, pokemons, potions):
    self.name = name
    self.pokemons = random.sample(pokemons, 6) if len(pokemons) > 6 else pokemons
    self.pokemon = self.pokemons[0]
    self.potions = potions

  def __repr__(self):
    print("Trainer {}, has these Pokemons:".format(self.name))
    for pokemon in self.pokemons:
      print(f"{pokemon.name}:   LVL:  {pokemon.level}, HP:  {pokemon.max_health}")
    return "Currently active Pokemon: {}".format(self.pokemon.name)

  def attack(self, other):
    if (self.pokemon.is_knocked_out == False and self.pokemon.max_health != 1) and (other.pokemon.is_knocked_out == False and other.pokemon.max_health != 1) :
      speed_count = 0
      if speed_count == 0:
        speed_count += 1
        if other.pokemon.speed > self.pokemon.speed:
          print("{}, faster than {}. {} has an advantage of attacking {}.".format(other.pokemon.name, self.pokemon.name, other.pokemon.name, self.pokemon.name))
          other.pokemon.attack(self.pokemon)
        else:
          self.pokemon.attack(other.pokemon)
      else:
        self.pokemon.attack(other.pokemon)
    else:
      print(f'{self.pokemon.name} is knocked out, choose another pokemon {self.name}.')

  def use_potion(self, posion_count):
    if self.pokemon.is_knocked_out == True:
      is_knocked_out = True
      self.pokemon.knock_out()
    else:
      self.posion_count = posion_count
      self.potions -= self.posion_count
      print("{}, successfully used the potion. Remaining potions: {}".format(self.name, self.potions))
      self.pokemon.restore_health(5)

  def switch_pokemon(self, number):
    if self.pokemon == self.pokemons[number]:
      print("{} cannot switch active pokemon with active pokemon.".format(self.name))
    elif not self.pokemons[number].is_knocked_out:
      print("{} switched {} with {}".format(self.name, self.pokemon.name, self.pokemons[number].name))
      self.pokemon = self.pokemons[number]
    else:
      print("{} is knocked out. Choose another pokemon, {}.".format(self.pokemons[number], self.name))




class FireType(Pokemon):
  def __init__(self, name, level):
    super().__init__(name, level, "Fire")

class WaterType(Pokemon):
  def __init__(self, name, level):
    super().__init__(name, level, "Water")

class GrassType(Pokemon):
  def __init__(self, name, level):
    super().__init__(name, level, "Grass")

Charizard = FireType("Charizard", 8)
Ponyta = FireType("Ponyta", 6)
Moltres = FireType("Moltres", 6)
Arcanine = FireType("Arcanine", 5)
Magmar = FireType("Magmar", 7)

Squirtle = WaterType("Squirtle", 5)
Golduck = WaterType("Golduck", 6)
Gyarados = WaterType("Gyarados", 7)
Blastoise = WaterType("Blastoise", 8)
Psyduck = WaterType("Psyduck", 9)

Bulbasaur = GrassType("Bulbasaur", 8)
Bellossom = GrassType("Bellossom", 5)
Exeggutor = GrassType("Exeggutor", 8)
Gloom = GrassType("Gloom", 7)
Venusaur = GrassType("Venusaur", 9)

pokemon_list = [Charizard, Ponyta, Moltres, Arcanine, Magmar, Squirtle, Golduck, Gyarados, Blastoise, Psyduck, Bulbasaur, Bellossom, Exeggutor, Gloom, Venusaur]

ash_pokemon_list = random.sample(pokemon_list, 7)
misty_pokemon_list = []

for pokemon in pokemon_list:
  if pokemon not in ash_pokemon_list:
    misty_pokemon_list.append(pokemon)


ash_ketchum = Trainer("Ash Ketchum", ash_pokemon_list, 2)
misty = Trainer("Misty", misty_pokemon_list, 5)
print(ash_ketchum)
print(misty)
ash_ketchum.attack(misty)
misty.attack(ash_ketchum)
misty.switch_pokemon(4)
#ash_ketchum.switch_pokemon(3)
ash_ketchum.attack(misty)
#misty.use_potion(1)
misty.attack(ash_ketchum)
#ash_ketchum.use_potion(1)
