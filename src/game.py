from ui import UI;
from flet import Colors;
from player import Player;

class Game:
  def __init__(self, page = None):
    self.page = page;
    self.ui = UI(self, page);
    self.current_player = None;

    self.settings = {
      "text speed" : 0.01,
      "delay" : 1,
    };

    self.ui.clear();
    self.createPlayer();
    self.gameLoop();
    
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

    _class = None;

    while True:
      _class = self.ui.getInput().lower();
      if _class == "":
        self.ui.clearPrevLine();
        self.ui.animatedPrint("You must pick a class to begin your journey. Warrior or Mage", color = Colors.RED);
        continue;
      elif _class not in ["warrior", "mage"]:
        self.ui.clearPrevLine();
        self.ui.animatedPrint(f"Hmm... {_class} A noble choice, but such a path is not yet known in the world of Erodia.\nPlease choose one of the known paths: Warrior or Mage.", color = Colors.RED);
        continue;
      break;

    self.ui.animatedPrint(f"Interesting.. you chose {_class}?", color = Colors.BLUE);
    self.ui.animatedPrint(f"Not a bad choice {name} the {_class.upper()}.");

    self.current_player = Player(name, self);
    self.ui.animatedPrint("Here are your stats:");
    self.current_player.getStats();

    self.ui.awaitInput(True);

  def gameLoop(self):
    while True:
      option = self.ui.getInput();
      
      if option == "stats":
        self.current_player.getStats();
      

  

