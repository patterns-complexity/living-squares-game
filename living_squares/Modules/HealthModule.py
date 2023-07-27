from living_squares.Entities.Entity import Entity
from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionManager import ActionManager
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum
from living_squares.Modules.Module import Module

class HealthModule(Module):
  def __init__(self, parent: Entity, initial_health: int = 100, max_health: int = 150) -> None:
    super().__init__(parent)
    self.parent: Entity = parent
    self.health: int = initial_health
    self.max_health: int = max_health
    self.poison_amount: int = 0
    self.observes_actions: list[str] = [
      ActionsEnum.FED.value,
    ]
    self.dead: bool = False
    pass

  def tick(self) -> None:
    super().tick()
    pass

  def poison(self, amount: int) -> None:
    self.poison_amount += amount

  def damage(self, amount: int) -> None:
    self.health -= amount
    pass

  def heal(self, amount: int) -> None:
    self.health += amount
    pass

  def get_health(self) -> int:
    return self.health

  def on_action(self, action: Action) -> None:
    if action.name == ActionsEnum.FED.value:
      target_entity: object = action.payload["target"]
      if isinstance(target_entity, self.parent.__class__):
        if self.parent.id == target_entity.id:
          self.heal(action.payload["nutrition"])
          self.poison(action.payload["toxicity"])

  def main(self) -> None:
    if self.poison_amount > 0:
      self.poison_amount -= 1
      self.damage(1)

    if self.health <= 0 and not self.dead:
      self.dead = True
      ActionManager.send_action(
        Action(
          ActionsEnum.DIED.value,
          { "target": self.parent }
        )
      )
      self.parent.destroy()

    if self.health > self.max_health:
      self.health = self.max_health
    pass
