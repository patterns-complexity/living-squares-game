from typing import Any

from living_squares.Managers.Manager.Manager import Manager
from living_squares.Services.SocketService import SocketService

class SocketManager(Manager):
  _service: SocketService | None = None

  @classmethod
  def recv(cls, data: Any) -> None:
    print(data)
    pass

  @classmethod
  def run(cls, framerate: int = 120, *args: Any, **kwargs: Any) -> None:
    if cls._service is None:
      cls._service = SocketService(kwargs['port'])
    cls.run_threaded(cls._service.run, cls.recv, framerate)
