from pyglet.shapes import ShapeBase, Rectangle, Circle, Ellipse
from living_squares.Entities.Entity import Entity
from living_squares.Global.Transform import Transform
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum
from living_squares.Modules.Module import Module
from living_squares.Managers.ActionManager.Action import Action

class PygletRendererModule(Module):
  def __init__(
    self,
    parent: Entity,
    transform: Transform,
    shape_class: type[ShapeBase],
    color: tuple[int, int, int] = (255, 0, 0)
  ) -> None:
    super().__init__(parent)

    self.transform: Transform = transform

    self.shape = shape_class(
      x = transform.position.x,
      y = transform.position.y,
      width = transform.scale.x,
      height = transform.scale.y,
      color = color
    )

    if shape_class is Circle:
      self.shape.radius = transform.scale.x,

    if shape_class is Ellipse:
      self.shape.a = transform.scale.x,
      self.shape.b = transform.scale.y

    self.shape.anchor_x = transform.scale.x / 2
    self.shape.anchor_y = transform.scale.y / 2

    self.observes_actions: list[str] = [
      ActionsEnum.UPDATE_RENDER.value
    ]
    pass

  def update_shape(
    self,
    shape: ShapeBase,
  ) -> None:
    if isinstance(shape, Rectangle):
      shape.width = self.transform.scale.x
      shape.height = self.transform.scale.y
    elif isinstance(shape, Circle):
      shape.radius = self.transform.scale.x
    elif isinstance(shape, Ellipse):
      shape.a = self.transform.scale.x
      shape.b = self.transform.scale.y

    shape.x = self.transform.position.x
    shape.y = self.transform.position.y

  def on_action(self, action: Action) -> None:
    if not action.payload["target"] == self.parent:
      return

    if action.name == ActionsEnum.UPDATE_RENDER.value:
      transform: Transform = action.payload["transform"]
      self.transform = transform
      self.update_shape(self.shape)
    pass

  def main(self, delta_time: float) -> None:
    self.shape.draw()
    pass
