from abc import ABC, abstractmethod
from typing import Any

from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from living_squares.Entities.Entity import Entity

class IIntegratable(ABC):
  @abstractmethod
  def register_as_observer(self) -> None:
    pass

  @abstractmethod
  def main(self) -> None:
    pass

  @abstractmethod
  def on_action(self, action: Action) -> None:
    pass

  @abstractmethod
  def notify(
    self,
    action_name: ActionsEnum,
    payload: dict[str, Any],
    target: 'IIntegratable'
  ) -> None:
    pass

  @abstractmethod
  def tick(self) -> None:
    pass
