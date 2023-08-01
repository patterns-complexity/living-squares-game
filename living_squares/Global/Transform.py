from math import sqrt
from vector import VectorObject2D, obj as v

class Transform():
  def __init__(
    self,
    position: VectorObject2D,
    scale: VectorObject2D
  ) -> None:
    self.position: VectorObject2D = position
    self.scale: VectorObject2D = scale
    pass

  def distance_to(self, other: 'Transform') -> float:
    dx: float = float(abs(other.position.x - self.position.x))
    dy: float = float(abs(other.position.y - self.position.y))

    sum_squares = dx**2 + dy**2

    return sqrt(sum_squares)

  def is_overalpping(self, other: 'Transform') -> bool:
    parent_scale: VectorObject2D = self.scale
    other_scale: VectorObject2D = other.scale

    distance_x: float = float(abs(self.position.x - other.position.x))
    distance_y: float = float(abs(self.position.y - other.position.y)) 

    is_overlapping_x: bool = distance_x <= float(parent_scale.x / 2) + float(other_scale.x / 2)
    is_overlapping_y: bool = distance_y <= float(parent_scale.y / 2) + float(other_scale.y / 2)

    return is_overlapping_x and is_overlapping_y

  def move(self, direction: str, amount: float) -> None:
    if direction == "up":
      self.position.y += amount
    elif direction == "down":
      self.position.y -= amount
    elif direction == "left":
      self.position.x -= amount
    elif direction == "right":
      self.position.x += amount

  def relocate(self, x: float, y: float) -> None:
    self.position.x = x
    self.position.y = y

  def rescale(self, x: float, y: float) -> None:
    self.scale.x = x
    self.scale.y = y
