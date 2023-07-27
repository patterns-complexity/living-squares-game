from pyglet.shapes import ShapeBase

from living_squares.Modules.HealthModule import HealthModule
from living_squares.Modules.PositionModule import PositionModule
from living_squares.Modules.RendererModule import RendererModule

from living_squares.Entities.Entity import Entity

class PlayerEntity(Entity):
  def __init__(self, shape: ShapeBase):
    super().__init__()
    self.add_module(HealthModule(self, initial_health=100, max_health=150))
    self.add_module(RendererModule(self, shape=shape))
    self.add_module(PositionModule(self, x=shape.x, y=shape.y))

    for module in self.modules.values():
      module.register_as_observer()
