from abc import ABC, abstractmethod
from typing import Coroutine

class IServing(ABC):
  @abstractmethod
  async def run(self) -> Coroutine[None, None, None]:
    pass

  @abstractmethod
  async def stop(self) -> Coroutine[None, None, None]:
    pass
