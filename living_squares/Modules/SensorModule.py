from living_squares.Entities.Entity import Entity
from living_squares.Global.Transform import Transform
from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.EntityManager.EntityManager import EntityManager
from living_squares.Modules.Module import Module
from living_squares.Modules.TransformsModule import TransformsModule


class SensorModule(Module):
  def __init__(self, parent: Entity) -> None:
    super().__init__(parent)
    self.first_five: list[Entity] = []
    pass

  def sorting_method(self, entity: Entity) -> float:
    if not isinstance(entity, Entity) or not isinstance(self.parent, Entity):
      return 0

    entity_transforms_module: TransformsModule = entity.module('TransformsModule')
    parent_transforms_module: TransformsModule = self.parent.module('TransformsModule')

    entity_transform: Transform = entity_transforms_module.transform
    parent_transform: Transform = parent_transforms_module.transform

    return entity_transform.distance_to(parent_transform)

  def sort_by_distance(self, entities: list[Entity]) -> list[Entity]:
    return sorted(entities, key=self.sorting_method)

  def calculate_first_five(self) -> None:
    entities = EntityManager.get_entities().copy()
    sorted_entities = self.sort_by_distance(entities)
    sorted_entities.pop(0)
    self.first_five = sorted_entities[:5]

  def on_action(self, action: Action) -> None:
    pass

  def get_first_five(self) -> list[Entity]:
    return self.first_five

  def main(self, delta_time: float) -> None:
    self.calculate_first_five()
    pass
