from threading import Thread
from time import sleep
from typing import Any, Callable

from living_squares.Interfaces.IManaging import IManaging

class Manager(IManaging):
  _threads: dict[str, Thread] = {}

  @classmethod
  def save_thread(cls, thread_key: str, thread: Thread) -> None:
    cls._threads[thread_key] = thread
    cls._threads[thread_key].start()

  @classmethod
  def endless_target(
    cls,
    target: Callable[[Callable[[Any], None]], None],
    return_callback: Callable[[Any], None],
    framerate: int = 120
  ) -> None:
    while True:
      sleep(1 / framerate)
      target(return_callback)

  @classmethod
  def run_threaded(
    cls,
    target: Callable[[Callable[[Any], None]], None],
    return_callback: Callable[[Any], None],
    framerate: int = 120
  ) -> None:
    thread_key: str = cls.__name__ + '.' + target.__name__

    dict_thread = cls._threads.get(thread_key)

    if dict_thread is not None:
      if dict_thread.is_alive():
        return
      del cls._threads[thread_key]

    new_thread = Thread(target=cls.endless_target, args=(target, return_callback, framerate))
    cls.save_thread(thread_key, new_thread)
