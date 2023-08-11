from abc import ABC, abstractmethod
from typing import Any

class IManaging(ABC):
  @abstractmethod
  def run(self, framerate: int = 120, *args: Any, **kwargs: Any) -> None:
    pass
