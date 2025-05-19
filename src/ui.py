import flet as ft;
from time import sleep;

class UI:
  def __init__(self, page):
    self.page = page;
    self.output = ft.Ref[ft.ListView]();
    self.field = ft.Ref[ft.TextField]();

    self.setup();
    
    

  def setup(self):
    self.page.fonts = {"retro" : "EightBitDragon-anqx.ttf"};
    self.page.theme = ft.Theme(font_family="retro");
    self.__createInterface();
  
  def __createInterface(self):
    self.page.add(
      ft.Column(
        controls = [
          ft.Container(
            content = ft.ListView(
              ref = self.output,
              auto_scroll = True
            ),
            
            expand = True,
            height = self.page.height * 0.9,
            border_radius=10,

          ),
          ft.TextField(ref = self.field, border_color = ft.Colors.GREEN, border_width = 3, on_submit = self.onFieldSubmit),
        ]
      )
    );

  def print(self, msg, color = ft.Colors.BLACK):
    self.output.current.controls.append(ft.Text(f"{msg}\n", color = color));
    self.page.update();

  def onFieldSubmit(self, e):
    self.print(e.control.value);
    e.control.value = "";
    self.page.update();