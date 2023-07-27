from living_squares.Entities.Entity import Entity
from living_squares.Managers.ActionManager.ActionManager import ActionManager
from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum
from living_squares.Modules.Module import Module

class PositionModule(Module):
  def __init__(self, parent: Entity, x: int, y: int) -> None:
    super().__init__(parent)
    self.x: int = x
    self.y: int = y
    self.observes_actions: list[str] = [
      ActionsEnum.MOVE.value
    ]
    pass

  def on_action(self, action: Action) -> None:
    if action.name == ActionsEnum.MOVE.value:
      direction = action.payload["direction"]

      if direction == "up":
        self.y += 1
      elif direction == "down":
        self.y -= 1
      elif direction == "left":
        self.x -= 1
      elif direction == "right":
        self.x += 1

    ActionManager.send_action(
      Action(
        ActionsEnum.UPDATE_RENDER.value,
        { "x": self.x, "y": self.y }
      )
    )
