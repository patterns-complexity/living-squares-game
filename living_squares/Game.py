from pyglet import app
from pyglet.window import Window
from pyglet.shapes import Rectangle

from random import randint

from living_squares.Entities.Entity import Entity
from living_squares.Entities.PlayerEntity import PlayerEntity
from living_squares.Entities.FoodEntity import FoodEntity

class LivingSquaresGame():
  def __init__(self, food_count: int = 20):
    self.food_count: int = food_count

    self.window: Window = Window()

    self.player: PlayerEntity = PlayerEntity(
      shape=Rectangle(
        x=self.window.height // 2,
        y=self.window.width // 2,
        width=10,
        height=10,
        color=(255, 0, 0)
      )
    )

    self.map_entities: list[Entity] = []

    self.window.on_draw = self.draw

  def draw(self) -> None:
    self.window.clear()
    self.player.tick()
    for entity in self.map_entities:
      entity.tick()
    pass

  def run(self) -> None:
    for _ in range(self.food_count):
      self.map_entities.append(
        FoodEntity(
          shape=Rectangle(
            x=randint(0, self.window.width),
            y=randint(0, self.window.height),
            width=5,
            height=5,
            color=(0, 255, 0)
          )
        )
      )
    app.run()
