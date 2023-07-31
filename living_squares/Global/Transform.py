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

  def distance_to(self, other: 'Transform') -> int:
    dx = other.position.x - self.position.x
    dy = other.position.y - self.position.y

    sum_squares = dx**2 + dy**2

    return sqrt(sum_squares)

  def is_overalpping(self, other: 'Transform') -> bool:
    parent_scale: VectorObject2D = self.scale
    other_scale: VectorObject2D = other.scale

    distance_x: int = abs(self.position.x - other.position.x)
    distance_y: int = abs(self.position.y - other.position.y)

    is_overlapping_x: bool = distance_x < parent_scale.x + other_scale.x
    is_overlapping_y: bool = distance_y < parent_scale.y + other_scale.y

    return is_overlapping_x or is_overlapping_y

  def move(self, direction: str, amount: int) -> None:
    if direction == "up":
      self.position.y += amount
    elif direction == "down":
      self.position.y -= amount
    elif direction == "left":
      self.position.x -= amount
    elif direction == "right":
      self.position.x += amount

  def relocate(self, x: int, y: int) -> None:
    self.position.x = x
    self.position.y = y

  def rescale(self, x: int, y: int) -> None:
    self.scale.x = x
    self.scale.y = y