import flet as ft;
from time import sleep;

class UI:
  def __init__(self, page = None):
    self.page = page;
    self.inputState = None;
    if page != None: self.setup();
    
  def setup(self):
    self.output = ft.Ref[ft.ListView]();
    self.field = ft.Ref[ft.TextField]();

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
    if self.page is None:
      return print(msg);
      
    self.output.current.controls.append(ft.Text(f"{msg}\n", color = color));
    self.page.update();
  
  
  def animatedPrint(self, msg, color = ft.Colors.BLACK):
    if self.page is None:
      for ch in msg:
        print(ch, end = "", flush = True);
        sleep(0.5);
        
    text = ft.Text(f"{msg[0]}\n", color = color);
    self.output.current.controls.append(text);
    self.page.update();
    
    for ch in text[1:]:
      text.value += ch;
      self.page.update();
      sleep(0.5);
    
  def getInput(self):
    if self.page is None:
      return input();
      
    self.inputState = "waiting";
    while self.inputState == "waiting":
      pass;
    return self.input;
  
  def onFieldSubmit(self, e):
    self.print(e.control.value);
    self.input = e.control.value;

    e.control.value = "";
    self.inputState = None;
    self.page.update();