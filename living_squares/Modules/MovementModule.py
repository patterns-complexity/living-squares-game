from living_squares.Entities.Entity import Entity
from living_squares.Global.Transform import Transform, v
from living_squares.Managers.ActionManager.ActionManager import ActionManager
from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum
from living_squares.Modules.Module import Module

class MovementModule(Module):
  def __init__(
    self,
    parent: Entity,
    transform: Transform,
  ) -> None:
    super().__init__(parent)
    self.transform: Transform = transform
    self.observes_actions: list[str] = [
      ActionsEnum.MOVE.value
    ]
    pass


  def on_action(self, action: Action) -> None:
    if action.name == ActionsEnum.MOVE.value:
      direction = action.payload["direction"]

      self.transform.move(direction, 10)

      self.notify(
        ActionsEnum.UPDATE_POSITION,
        { "transform": self.transform },
        self.parent
      )
