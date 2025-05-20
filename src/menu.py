class Menu:
  def __init__(self, game, ui):
    self.game = game;
    self.ui = ui;
    
  def mainMenu(self):
    self.ui.print("== ComplexRPG ==");
    self.ui.print("1. start");
    self.ui.print("2. quit");
    
    self.ui.print(f"you said {self.ui.getInput()}");