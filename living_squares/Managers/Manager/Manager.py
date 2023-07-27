import asyncio
from queue import Queue

from threading import Thread
from typing import Coroutine
from living_squares.Interfaces.IQueuable import IQueueable

from living_squares.Services.Service import Service

class Manager():
  _threads: dict[Thread, Queue[IQueueable]] = {}

  @classmethod
  def run_service(cls, service: Service) -> None:
    service_coroutine: Coroutine[None, None, Coroutine[None, None, None]] = service.run()
    loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()
    loop.create_task(service_coroutine)
    loop.run_forever()
  pass

