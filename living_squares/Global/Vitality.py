class Vitality():
  def __init__(
    self,
    health: int,
    max_health: int = 150,
    poison_amount: int = 0,
    max_poison_amount: int = 100,
    dead: bool = False
  ) -> None:
    self.initial_health: int = health
    self.health: int = health
    self.max_health: int = max_health
    self.poison_amount: int = poison_amount
    self.max_poison_amount: int = max_poison_amount
    self.dead: bool = dead
    self.tick_counter: int = 0

  def death_check(self) -> bool:
    if self.dead:
      return True

    if self.health <= 0:
      self.dead = True
      return True
    return False

  def health_bounds_check(self) -> None:
    if self.health > self.max_health:
      self.health = self.max_health

    if self.health < 0:
      self.health = 0

  def revive(self) -> None:
    self.dead = False
    self.health = self.initial_health
    self.poison_amount = 0

  def poison(self, amount: int) -> None:
    self.poison_amount += amount

  def detox(self, amount: int) -> None:
    self.poison_amount -= amount

  def damage(self, amount: int) -> None:
    self.health -= amount

  def heal(self, amount: int) -> None:
    self.health += amount

  def get_health(self) -> int:
    return self.health

  def is_alive_tick(self) -> bool:
    if self.poison_amount > 0:
      self.detox(1)
      self.damage(1)
    if self.tick_counter > 10:
      self.tick_counter = 0
      self.damage(1)
    self.tick_counter += 1

    print(self.health)

    self.health_bounds_check()
    if self.death_check():
      return False
    return True
