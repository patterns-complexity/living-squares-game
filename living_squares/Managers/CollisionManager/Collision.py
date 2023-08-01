from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from living_squares.Entities.Entity import Entity

class Collision():
  def __init__(self, source: 'Entity', target: 'Entity') -> None:
    self.source: 'Entity' = source
    self.target: 'Entity' = target
    pass

  def __str__(self) -> str:
    ids: list[str] = [str(self.source.id), str(self.target.id)]
    sorted_ids: list[str] = sorted(ids)
    joined_ids: str = "-".join(sorted_ids)
    return joined_ids

  def __eq__(self, other: object) -> bool:
    if not isinstance(other, Collision):
      raise NotImplementedError(f"Cannot compare Collision to {type(other)}")
    return self.__str__() == other.__str__()
