from living_squares.Entities.Entity import Entity
from living_squares.Global.Vitality import Vitality
from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum
from living_squares.Modules.Module import Module

class HealthModule(Module):
  def __init__(
    self, parent: Entity,
    initial_health: int = 100,
    max_health: int = 150
  ) -> None:
    super().__init__(parent)
    self.parent: Entity = parent
    self.vitality = Vitality(initial_health, max_health)
    self.observes_actions: list[str] = [
      ActionsEnum.FED.value,
    ]
    pass

  def on_action(self, action: Action) -> None:
    if not action.payload["target"] == self.parent:
      return

    if action.name == ActionsEnum.FED.value:
      self.vitality.heal(action.payload["nutrition"])
      self.vitality.poison(action.payload["toxicity"])

  def main(self, delta_time: float) -> None:
    vitality_tick_result: bool = self.vitality.is_alive_tick()
    if vitality_tick_result is False:
      self.notify(
        ActionsEnum.DIED,
        {},
        self.parent
      )
      if isinstance(self.parent, Entity):
        self.parent.destroy()
