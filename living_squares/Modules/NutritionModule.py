from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum
from living_squares.Managers.CollisionManager.Collision import Collision

from living_squares.Modules.Module import Module

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from living_squares.Entities.Entity import Entity
class NutritionModule(Module):
  def __init__(self, parent: 'Entity') -> None:
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
      if (collision.source.id == self.parent.id or collision.target.id == self.parent.id):
        other: 'Entity' = collision.source if collision.target.id == self.parent.id else collision.target
        self.notify(
          ActionsEnum.FED,
          { "nutrition": self.nutrition, "toxicity": self.toxicity },
          other
        )
        self.parent.destroy()
