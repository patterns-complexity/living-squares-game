from living_squares.Entities.Entity import Entity
from living_squares.Entities.FoodEntity import FoodEntity
from living_squares.Entities.PlayerEntity import PlayerEntity
from living_squares.Managers.ActionManager.ActionManager import ActionManager
from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum
from living_squares.Modules.HealthModule import HealthModule
from living_squares.Modules.Module import Module

class NutritionModule(Module):
  def __init__(self, parent: Entity) -> None:
    super().__init__(parent)
    self.nutrition: int = 0
    self.toxicity: int = 0
    self.observes_actions: list[str] = [
      ActionsEnum.CONSUMED.value
    ]
    pass

  def on_action(self, action: Action) -> None:
    if action.name == ActionsEnum.CONSUMED.value:
      target_entity: object = action.payload["target"]
      source_entity: object = action.payload["source"]

      if isinstance(target_entity, FoodEntity) and isinstance(source_entity, PlayerEntity):
        source_entity_module: Module = source_entity.module("HealthModule")
        if isinstance(source_entity_module, HealthModule):

          ActionManager.send_action(
            Action(
              ActionsEnum.FED.value,
              {
                "target": source_entity,
                "source": target_entity,
                "nutrition": self.nutrition,
                "toxicity": self.toxicity
              },
            )
          )
