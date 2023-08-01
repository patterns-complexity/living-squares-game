from typing import Callable
from pyglet import app
from pyglet.window import Window

class Game():
  def __init__(self) -> None:
    self.window: Window = Window()

  def draw(self) -> None:
    self.window.clear()

  def prepare(self) -> None:
    pass

  def run(self) -> None:
    self.prepare()
    app.run()
