from abc import ABC, abstractmethod
from os import PathLike

from living_squares.Managers.InputManager.ControlSchemeEnum import ControlSchemeEnum
from living_squares.Managers.ActionManager.Action import Action

class IMappable(ABC):
  @property
  @abstractmethod
  def scheme(self) -> dict[int, Action]:
    pass

  @property
  @abstractmethod
  def type(self) -> ControlSchemeEnum:
    pass

  @abstractmethod
  def modify(self, key: int, action: Action) -> None:
    pass

  @abstractmethod
  def load(self, path: PathLike[str]) -> None:
    pass

  @abstractmethod
  def save(self, path: PathLike[str]) -> None:
    pass
