from uuid import UUID
from living_squares.Entities.Entity import Entity
from living_squares.Global.Transform import Transform
from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionManager import ActionManager
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum
from living_squares.Managers.EntityManager.EntityManager import EntityManager
from living_squares.Modules.TransformsModule import TransformsModule

class CollisionManager():
  @classmethod
  def transforms_colliding(cls, obj1: Transform, obj2: Transform) -> bool:
    return obj1.is_overalpping(obj2)

  @classmethod
  def entities_colliding(cls, entity: Entity) -> list[dict[str, Entity]]:
    entities: list[Entity] = EntityManager.get_entities()
    collisions: list[dict[str, Entity]] = []

    for other_entity in entities:
      if other_entity.id == entity.id:
        continue

      transforms_module: TransformsModule = entity.module("TransformsModule")
      other_transforms_module: TransformsModule = other_entity.module("TransformsModule")

      transform: Transform = transforms_module.transform
      other_transform: Transform = other_transforms_module.transform

      if cls.transforms_colliding(transform, other_transform):
        collisions.append({
          "source": entity,
          "target": other_entity
        })

    return collisions

  @classmethod
  def tick(cls) -> None:
    entities: list[Entity] = EntityManager.get_entities()
    entities_checked: list[UUID] = []
    all_collisions: list[dict[str, Entity]] = []

    for entity in entities:
      collisions: list[dict[str, Entity]] = cls.entities_colliding(entity)
      for collision in collisions:
        if (collision["source"].id in entities_checked or collision["target"].id in entities_checked):
          continue

        entities_checked.append(collision["source"].id)
        entities_checked.append(collision["target"].id)
        all_collisions.append(collision)

    # TODO: add collision Action sending
