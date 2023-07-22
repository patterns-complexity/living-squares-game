from __future__ import annotations

from uuid import UUID, uuid4

from living_squares.Interfaces.IIntegratable import IIntegratable

from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum

from living_squares.Managers.ActionManager.ActionManager import ActionManager

class Module(IIntegratable):
  def __init__(self, id: UUID = uuid4()) -> None:
    self.id: UUID = id
    self.name: str = self.__class__.__name__
    self.observes_actions: list[ActionsEnum] = []
    pass

  def __str__(self) -> str:
    return self.name

  def __repr__(self) -> str:
    return self.__str__()

  def __eq__(self, o: object) -> bool:
    if isinstance(o, Module):
      return self.id == o.id
    return False

  def register_as_observer(self) -> None:
    ActionManager.register_observer(self)
    pass

  def on_action(self, action: Action) -> None:
    print(f"{self} received {action}")
    pass

  def main(self) -> None:
    pass

  def on_key_press(self, symbol: int, modifiers: int) -> None:
    pass

  def tick(self) -> None:
    self.main()
    pass
