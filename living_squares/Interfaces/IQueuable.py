from abc import ABC, abstractmethod

from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum

class IQueueable(ABC):
  @property
  @abstractmethod
  def name(self) -> ActionsEnum:
    pass

  @property
  @abstractmethod
  def payload(self) -> dict[str, str | int]:
    pass
