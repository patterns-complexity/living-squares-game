from typing import Any, Callable
from living_squares.Entities.Entity import Entity
from living_squares.Managers.EntityManager.EntityManager import EntityManager
from living_squares.Services.Service import Service

class CollisionService(Service):
  def __init__(self) -> None:
    super().__init__()
    pass

  def run(self, callback: Callable[[Any], None]) -> None:
    entities: list[Entity] = EntityManager.get_entities()

    for entity in entities:
      callback(entity)
