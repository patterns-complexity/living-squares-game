from pyglet.shapes import ShapeBase

from living_squares.Entities.Entity import Entity

from living_squares.Modules.RendererModule import RendererModule

class FoodEntity(Entity):
  def __init__(self, shape: ShapeBase):
    super().__init__()
    self.add_module(RendererModule(shape=shape))
    pass
