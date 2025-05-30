import flet as ft;
from time import sleep;

class UI:
  def __init__(self, game, page = None):
    self.page = page;
    self.waitingInput = False;
    if page != None: self.setup();
    
    self.game = game; 

  def setup(self):
    self.output = ft.Ref[ft.ListView]();
    self.field = ft.Ref[ft.TextField]();

    self.page.fonts = {"retro" : "EightBitDragon-anqx.ttf"};
    self.page.theme = ft.Theme(font_family="retro");
    self.page.theme_mode = ft.ThemeMode.LIGHT;
    self.__createInterface();
  
  def __createInterface(self):
    self.page.bgcolor = ft.Colors.BLACK
    self.page.padding = 20

    neon_purple = "#ff00ff"
    neon_blue = "#00ffff"
    neon_green = "#39ff14"
    neon_shadow = ft.Colors.with_opacity(0.5, neon_purple)

    self.page.add(
        ft.SafeArea(  
            ft.Column(
                spacing=12,
                controls=[
                    ft.Container(
                        content=ft.ListView(
                            ref=self.output,
                            auto_scroll=True,
                        ),
                        expand=True,
                        height=self.page.height * 0.85,
                        bgcolor="#111111",
                        border_radius=10,
                        padding=20,
                        border=ft.border.all(2, neon_blue),
                        shadow=ft.BoxShadow(
                            blur_radius=15,
                            color=neon_shadow,
                            offset=ft.Offset(0, 0),
                            spread_radius=2
                        )
                    ),
                    ft.TextField(
                        ref=self.field,
                        hint_text="> Enter command...",
                        text_style=ft.TextStyle(
                            color=neon_green,
                            font_family="Courier New",
                            size=16,
                        ),
                        bgcolor="#1a1a1a",
                        border_color=neon_green,
                        border_width=2,
                        cursor_color=neon_green,
                        focused_border_color=neon_blue,
                        height=50,
                        on_submit=self.onFieldSubmit,
                        hint_style=ft.TextStyle(
                            color=ft.Colors.with_opacity(0.4, neon_green),
                            font_family="Courier New"
                        )
                    ),
                ]
            )
        )
    )

  def print(self, msg, color = ft.Colors.WHITE):
    if self.page is None:
      return print(msg);
      
    self.output.current.controls.append(ft.Text(f"{msg}\n", color = color));
    self.page.update();
  
  
  def animatedPrint(self, msg, color = ft.Colors.WHITE):
    if self.page is None:
      for ch in msg:
        print(ch, end = "", flush = True);
        sleep(self.game.settings["text speed"]);
      return;

    text = ft.Text(f"", color = color);
    self.output.current.controls.append(text);
    self.page.update();
    
    for ch in msg:
      text.value += ch;
      self.page.update();
      sleep(self.game.settings["text speed"]);

    text.value += "\n";
    self.page.update();
    sleep(self.game.settings["delay"]);

  def getInput(self):
    if self.page is None:
      return input();
      
    self.waitingInput = True;
    while self.waitingInput is True:
      pass;
    return self.input;
  
  def awaitInput(self, clear = False):
    self.print("enter anyting to continue!", color = ft.Colors.RED);
    _ = self.getInput();
    if clear is True: self.clear();

  def clearPrevLine(self):
    if self.page != None: self.output.current.controls.pop();
    self.page.update();

  def clear(self):
    if self.page != None: self.output.current.controls.clear();
    self.page.update();

  def onFieldSubmit(self, e):
    if e.control.value != "": self.print(f"> {e.control.value}");
    self.input = e.control.value;

    e.control.value = "";
    self.waitingInput = False;
    self.page.update();
