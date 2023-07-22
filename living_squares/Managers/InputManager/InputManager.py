from living_squares.Managers.ActionManager.ActionManager import ActionManager
from living_squares.Managers.ActionManager.Action import Action

from living_squares.Managers.InputManager.ControlScheme import ControlScheme

class InputManager():
  _control_scheme: dict[int, Action] = ControlScheme().scheme

  @classmethod
  def handle_press(cls, symbol: int, modifiers: int) -> None:
    if symbol in cls._control_scheme:
      ActionManager.send_action(cls._control_scheme[symbol])
