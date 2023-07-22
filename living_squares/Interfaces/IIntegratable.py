from abc import ABC, abstractmethod

from living_squares.Managers.ActionManager.Action import Action

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
  def tick(self) -> None:
    pass
