from abc import ABC, abstractmethod
from typing import Any, Callable

class IServing(ABC):
  @abstractmethod
  def run(self, callback: Callable[[Any], None]) -> None:
    pass
