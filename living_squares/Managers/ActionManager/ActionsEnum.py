from enum import Enum

class ActionsEnum(Enum):
  UPDATE_RENDER = "update_renderer"
  UPDATE_POSITION = "update_transform"
  UPDATE_SCALE = "update_scale"
  MOVE = "move"
  CONSUMED = "consumed"
  FED = "fed"
  DIED = "died"
