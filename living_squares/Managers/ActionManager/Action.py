from living_squares.Interfaces.IQueuable import IQueueable

from typing import Any

class Action(IQueueable):
  def __init__(self, name: str, payload: dict[ str, Any ]) -> None:
    self._name: str = name
    self._payload: dict[ str, Any ] = payload

  @property
  def name(self) -> str:
    return self._name

  @property
  def payload(self) -> dict[ str, Any ]:
    return self._payload
