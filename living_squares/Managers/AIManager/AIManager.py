from living_squares.Managers.ActionManager.Action import Action
from living_squares.Managers.ActionManager.ActionManager import ActionManager
from living_squares.Managers.ActionManager.ActionsEnum import ActionsEnum
from living_squares.Managers.Manager.Manager import Manager


class AIManager(Manager):
  def __init__(self) -> None:
    super().__init__()

  def move(self, direction: str) -> None:
    ActionManager.send_action(
      Action(
        ActionsEnum.MOVE.value,
        { "direction": direction }
      )
    )

