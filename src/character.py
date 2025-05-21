class Character:
  def __init__(self, name):
    self.name = name;
    self.level = 1;
    self.exp = 0;

    self.health = 100;
    self.max_health = 100;

    self.energy = 100;
    self.max_energy = 100;

    self.money = {
      "gold" : 0,
      "silver" : 0,
      "copper" : 0,
    };

    self.stats = {
      "strength" : 0,
      "defense" : 0,
      "dexterity" : 0,
      "luck" : 0,
    };

    