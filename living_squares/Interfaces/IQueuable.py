from abc import ABC, abstractmethod
from typing import Any

class IQueueable(ABC):
  @property
  @abstractmethod
  def name(self) -> str:
    pass

  @property
  @abstractmethod
  def payload(self) -> dict[ str, Any ]:
    pass
