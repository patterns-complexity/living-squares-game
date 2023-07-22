from living_squares.Modules.Module import Module

class HealthModule(Module):
  def __init__(self) -> None:
    super().__init__()
    self.health: int = 100
    pass

  def tick(self) -> None:
    super().tick()
    pass

  def damage(self, amount: int) -> None:
    self.health -= amount
    pass

  def heal(self, amount: int) -> None:
    self.health += amount
    pass

  def get_health(self) -> int:
    return self.health

  def main(self) -> None:
    pass
