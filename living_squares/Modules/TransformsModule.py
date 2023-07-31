from living_squares.Entities.Entity import Entity
from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum
from living_squares.Modules.Module import Module
from living_squares.Global.Transform import Transform

class TransformsModule(Module):
  def __init__(
    self,
    parent: Entity,
    transform: Transform,
  ) -> None:
    super().__init__(parent)

    self.transform: Transform = transform

    self.observes_actions: list[str] = [
      ActionsEnum.UPDATE_POSITION.value,
      ActionsEnum.UPDATE_SCALE.value
    ]
    pass

  def on_action(self, action: Action) -> None:
    if action.payload["target"] != self.parent:
      return

    transform: Transform = action.payload["transform"]

    if action.name == ActionsEnum.UPDATE_POSITION.value:
      self.transform.relocate(
        transform.position.x,
        transform.position.y
      )

    if action.name == ActionsEnum.UPDATE_SCALE.value:
      self.transform.rescale(
        transform.scale.x,
        transform.scale.y
      )

    self.notify(
      ActionsEnum.UPDATE_RENDER,
      { "transform": self.transform },
      self.parent
    )
