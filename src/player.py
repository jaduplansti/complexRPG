from character import Character; 
from flet import Colors;
class Player(Character):
  def __init__(self, name, game):
    super().__init__(name);
    self.game = game;

  def getStats(self):
    for n, stat in enumerate(self.stats):
      self.game.ui.animatedPrint(f"| {stat}: {self.stats[stat]} |", color = [Colors.YELLOW, Colors.BROWN, Colors.INDIGO, Colors.PURPLE][n]);
