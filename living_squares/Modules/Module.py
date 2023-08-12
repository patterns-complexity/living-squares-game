from __future__ import annotations

from uuid import UUID, uuid4

from living_squares.Interfaces.IIntegratable import IIntegratable

from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionManager import ActionManager
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
  from living_squares.Entities.Entity import Entity

class Module(IIntegratable):
  def __init__(self, parent: Entity, id: UUID = uuid4()) -> None:
    self.id: UUID = id
    self.parent: Entity = parent
    self.name: str = self.__class__.__name__
    self.observes_actions: list[str] = []
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

  def notify(
    self,
    action_name: ActionsEnum,
    payload: dict[str, Any],
    target: Entity | None = None
  ) -> None:
    if target is not None:
      payload["target"] = target

    ActionManager.send_action(
      Action(
        action_name.value,
        payload
      )
    )
    pass

  def main(self, delta_time: float) -> None:
    pass

  def tick(self, delta_time: float) -> None:
    self.main(delta_time)
    pass
