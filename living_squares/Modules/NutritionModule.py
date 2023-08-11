from typing import cast
from living_squares.Interfaces.IIntegratable import IIntegratable
from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum
from living_squares.Managers.CollisionManager.Collision import Collision

from living_squares.Modules.Module import Module

from living_squares.Entities.Entity import Entity

class NutritionModule(Module):
  def __init__(self, parent: IIntegratable) -> None:
    super().__init__(parent)
    self.nutrition: int = 15
    self.toxicity: int = 0
    self.observes_actions: list[str] = [
      ActionsEnum.COLLISION_DETECTED.value
    ]
    pass

  def on_action(self, action: Action) -> None:
    if action.name == ActionsEnum.COLLISION_DETECTED.value:
      collision: Collision = action.payload["collision"]
      if (
        isinstance(collision.source, Entity)
          and isinstance(collision.target, Entity)
          and isinstance(self.parent, Entity)
          and (
            collision.source.id == self.parent.id
              or collision.target.id == self.parent.id
          )
      ):

        other: Entity

        if collision.source.id == self.parent.id:
          other = collision.target
        elif collision.target.id == self.parent.id:
          other = collision.source

        self.notify(
          ActionsEnum.FED,
          { "nutrition": self.nutrition, "toxicity": self.toxicity },
          cast(IIntegratable, other)
        )
        self.parent.destroy()
