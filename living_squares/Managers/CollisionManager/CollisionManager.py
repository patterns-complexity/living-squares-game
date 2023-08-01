from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from living_squares.Entities.Entity import Entity

from living_squares.Global.Transform import Transform
from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionManager import ActionManager
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum
from living_squares.Managers.CollisionManager.Collision import Collision
from living_squares.Managers.EntityManager.EntityManager import EntityManager

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from living_squares.Modules.TransformsModule import TransformsModule

class CollisionManager():
  _all_collisions: list[Collision] = []

  @classmethod
  def is_stale_collision(cls, transforms_colliding: bool, collision: Collision) -> bool:
    return (not transforms_colliding) and (collision in cls._all_collisions)

  @classmethod
  def is_new_collision(cls, transforms_colliding: bool, collision: Collision) -> bool:
    return transforms_colliding and (collision not in cls._all_collisions)

  @classmethod
  def notify(cls, action_name: ActionsEnum, collision: Collision) -> None:
    ActionManager.send_action(
      Action(
        action_name.value,
        { "collision": collision }
      )
    )

  @classmethod
  def transforms_colliding(cls, entity: 'Entity', other_entity: 'Entity') -> bool:
    transforms_module: TransformsModule = entity.module("TransformsModule")
    other_transforms_module: TransformsModule = other_entity.module("TransformsModule")

    transform: Transform = transforms_module.transform
    other_transform: Transform = other_transforms_module.transform

    return transform.is_overalpping(other_transform)

  @classmethod
  def check_collisions(cls, entity: 'Entity') -> None:
    entities: list[Entity] = EntityManager.get_entities()

    for other_entity in entities:
      if other_entity.id == entity.id:
        continue

      transforms_colliding: bool = cls.transforms_colliding(entity, other_entity)

      collision: Collision = Collision(entity, other_entity)

      if cls.is_new_collision(transforms_colliding, collision):
        cls._all_collisions.append(collision)
        cls.notify(ActionsEnum.COLLISION_DETECTED, collision)

      if cls.is_stale_collision(transforms_colliding, collision):
        cls._all_collisions.remove(collision)
        cls.notify(ActionsEnum.COLLISION_STOPPED, collision)

  @classmethod
  def tick(cls) -> None:
    entities: list[Entity] = EntityManager.get_entities()

    for entity in entities:
      cls.check_collisions(entity)
