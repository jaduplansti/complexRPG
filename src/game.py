from ui import UI;
from flet import Colors;

class Game:
  def __init__(self, page = None):
    self.page = page;
    self.ui = UI(self, page);
    self.current_player = None;

    self.settings = {
      "text speed" : 0.01,
      "delay" : 1,
    };

    self.createPlayer();

  def createPlayer(self):
    self.ui.print("Welcome to the world of erodia, adventurer what is your name?");
    
    while True:
      name = self.ui.getInput();
      if name == "":
        self.ui.clearPrevLine();
        self.ui.animatedPrint("You must have a name to begin your journey.", color = Colors.RED);
        continue;
      break;

    self.ui.animatedPrint(f"Ah, {name} A fine name for a hero.");
    self.ui.animatedPrint("Now, choose a basic class.");
    self.ui.animatedPrint("- Warrior, strong and fearless, master of brute force.", color = Colors.INDIGO);
    self.ui.animatedPrint("- The Mage, wise and mysterious, wielder of arcane power.", Colors.PURPLE);

    while True:
      _class = self.ui.getInput();
      if _class == "":
        self.ui.clearPrevLine();
        self.ui.animatedPrint(" You must pick a class to begin your journey. Warrior or Mage", color = Colors.RED);
        continue;
      elif _class not in ["Warrior", "Mage"]:
        self.ui.clearPrevLine();
        self.ui.animatedPrint(f"Hmm... {_class} A noble choice, but such a path is not yet known in the world of Erodia.\nPlease choose one of the known paths: Warrior or Mage.", color = Colors.RED);
        continue;
      break;

  

