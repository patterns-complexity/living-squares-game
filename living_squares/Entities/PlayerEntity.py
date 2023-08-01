from pyglet.window import Window
from pyglet.shapes import Rectangle

from living_squares.Entities.Entity import Entity
from living_squares.Global.Transform import Transform, v

from living_squares.Modules.HealthModule import HealthModule
from living_squares.Modules.MovementModule import MovementModule
from living_squares.Modules.PygletRendererModule import PygletRendererModule
from living_squares.Modules.TransformsModule import TransformsModule

class PlayerEntity(Entity):
  def __init__(self, window:Window) -> None:
    super().__init__()
    self.window: Window = window

  def setup(self) -> None:
    x: float = self.window.width / 2
    y: float = self.window.height / 2

    scale_x: float = 10
    scale_y: float = 10

    transform: Transform = Transform(
      v(x=x, y=y),
      v(x=scale_x, y=scale_y),
    )

    self.add_module(PygletRendererModule(
      self,
      transform,
      Rectangle,
      color=(255, 0, 0)
    ))
    self.add_module(TransformsModule(
      self,
      transform
    ))
    self.add_module(MovementModule(
      self,
      transform
    ))
    self.add_module(HealthModule(
      self, initial_health=100, max_health=150
    ))
