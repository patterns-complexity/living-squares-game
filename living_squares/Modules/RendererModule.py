from pyglet.shapes import ShapeBase

from living_squares.Modules.Module import Module

class RendererModule(Module):
  def __init__(self, shape: ShapeBase) -> None:
    super().__init__()
    self.shape: ShapeBase = shape
    pass

  def main(self) -> None:
    self.shape.draw()
    pass