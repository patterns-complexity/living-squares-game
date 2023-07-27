from __future__ import annotations

from living_squares.Managers.ActionManager.Action import Action

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from living_squares.Modules.Module import Module

class ActionManager():
  _observers: dict[str, list[Module]] = {}

  @classmethod
  def register_observer(cls, observer: Module) -> None:
    if len(observer.observes_actions) == 0:
      return

    for action_name in observer.observes_actions:
      if action_name not in cls._observers:
        cls._observers[action_name] = []

      cls._observers[action_name].append(observer)

  @classmethod
  def send_action(cls, action: Action) -> None:
    if action.name not in cls._observers:
      return

    for observer in cls._observers[action.name]:
      observer.on_action(action)
