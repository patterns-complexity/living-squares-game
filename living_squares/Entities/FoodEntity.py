from random import randint

from pyglet.shapes import Rectangle
from pyglet.window import Window

from living_squares.Entities.Entity import Entity

from living_squares.Global.Transform import Transform, v

from living_squares.Modules.PygletRendererModule import PygletRendererModule
from living_squares.Modules.TransformsModule import TransformsModule

class FoodEntity(Entity):
  def __init__(self, window: Window) -> None:
    super().__init__()
    self.window: Window = window
    pass

  def setup(self) -> None:
    x: int = randint(0, self.window.width)
    y: int = randint(0, self.window.height)

    scale_x: int = 5
    scale_y: int = 5

    transform: Transform = Transform(
      v(x=x, y=y),
      v(x=scale_x, y=scale_y),
    )

    self.add_module(PygletRendererModule(
      self,
      transform,
      Rectangle,
      color=(0, 255, 0)
    ))

    self.add_module(TransformsModule(
      self,
      transform
    ))
