from json import load, dump

from os import PathLike

from living_squares.Interfaces.IMappable import IMappable

from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum

from living_squares.Managers.InputManager.KeysEnum import KeysEnum
from living_squares.Managers.InputManager.ControlSchemeEnum import ControlSchemeEnum

class ControlScheme(IMappable):
  def __init__(self) -> None:
    self._scheme: dict[int, Action] = {
      KeysEnum.W: Action(
        ActionsEnum.MOVE.value,
        { "direction": "up"}
      ),
      KeysEnum.A: Action(
        ActionsEnum.MOVE.value,
        { "direction": "left"}
      ),
      KeysEnum.S: Action(
        ActionsEnum.MOVE.value,
        { "direction": "down"}
      ),
      KeysEnum.D: Action(
        ActionsEnum.MOVE.value,
        { "direction": "right"}
      )
    }
    self._type: ControlSchemeEnum = ControlSchemeEnum.DEFAULT

  @property
  def scheme(self) -> dict[int, Action]:
    return self._scheme

  @property
  def type(self) -> ControlSchemeEnum:
    return self._type

  def modify(self, key: int, action: Action) -> None:
    self._scheme[key] = action

  def load(self, path: PathLike[str]) -> None:
    with open(path, "r") as file:
      data = load(file)
      self._scheme = data["scheme"]
      self._type = ControlSchemeEnum(data["type"])

  def save(self, path: PathLike[str]) -> None:
    with open(path, "w") as file:
      dump({
        "scheme": self._scheme,
        "type": self._type.value
      }, file, indent=2)
