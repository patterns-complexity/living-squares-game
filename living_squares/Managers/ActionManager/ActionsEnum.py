from enum import Enum

class ActionsEnum(Enum):
  UPDATE_RENDER = "update_renderer"
  UPDATE_POSITION = "update_transform"
  UPDATE_SCALE = "update_scale"
  COLLISION_DETECTED = "collision_detected"
  COLLISION_STOPPED = "collision_stopped"
  MOVE = "move"
  CONSUMED = "consumed"
  FED = "fed"
  DIED = "died"
