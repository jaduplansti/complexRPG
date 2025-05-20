from ui import UI;
from menu import Menu;

class Game:
  def __init__(self, page = None):
    self.page = page;
    self.ui = UI(page);
    self.menu = Menu(self, self.ui);
    self.current_player = None;
    
    self.menu.mainMenu();
    