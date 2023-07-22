from uuid import UUID, uuid4

from living_squares.Interfaces.IIntegratable import IIntegratable

class Module(IIntegratable):
  def __init__(self, id: UUID = uuid4()) -> None:
    self.id: UUID = id
    self.name: str = self.__class__.__name__
    pass

  def __str__(self) -> str:
    return self.name

  def __repr__(self) -> str:
    return self.__str__()

  def __eq__(self, o: object) -> bool:
    if isinstance(o, Module):
      return self.id == o.id
    return False

  def main(self) -> None:
    pass

  def tick(self) -> None:
    self.main()
    pass