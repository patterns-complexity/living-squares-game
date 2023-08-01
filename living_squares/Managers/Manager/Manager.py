from threading import Thread

from typing import Any, Callable

class Manager():
  @classmethod
  def tick_threaded(cls, target: Callable[[Callable[[Any], None]], None], return_callback: Callable[[Any], None]) -> None:
    thread: Thread = Thread(target=target, args=(return_callback,))
    thread.start()
