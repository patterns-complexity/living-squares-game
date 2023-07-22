from living_squares.Interfaces.IQueuable import IQueueable
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum

class Action(IQueueable):
  def __init__(self, name: ActionsEnum, payload: dict[str, str | int]) -> None:
    self._name: ActionsEnum = name
    self._payload: dict[str, str | int] = payload

  @property
  def name(self) -> ActionsEnum:
    return self._name

  @property
  def payload(self) -> dict[str, str | int]:
    return self._payload
