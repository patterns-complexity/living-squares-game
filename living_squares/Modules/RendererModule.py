from pyglet.shapes import ShapeBase
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum

from living_squares.Modules.Module import Module

from living_squares.Managers.ActionManager.Action import Action

class RendererModule(Module):
  def __init__(self, shape: ShapeBase) -> None:
    super().__init__()
    self.shape: ShapeBase = shape
    self.observes_actions: list[ActionsEnum] = [
      ActionsEnum.UPDATE_RENDER
    ]
    pass

  def on_action(self, action: Action) -> None:
    if action.name == ActionsEnum.UPDATE_RENDER:
      self.shape.x = action.payload["x"]
      self.shape.y = action.payload["y"]
    pass

  def main(self) -> None:
    self.shape.draw()
    pass
