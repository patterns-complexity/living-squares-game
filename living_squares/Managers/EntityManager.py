from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from living_squares.Entities.Entity import Entity

class EntityManager():
  _entities: list['Entity'] = []

  @classmethod
  def register_entity(cls: type['EntityManager'], entity: 'Entity') -> None:
    if entity in cls._entities:
      return

    cls._entities.append(entity)

  @classmethod
  def unregister_entity(cls: type['EntityManager'], entity: 'Entity') -> None:
    if entity not in cls._entities:
      return

    cls._entities.remove(entity)

