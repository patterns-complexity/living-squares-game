#%% Project imports
from time import time

from living_squares.Game import Game

from living_squares.Managers.CollisionManager.CollisionManager import CollisionManager
from living_squares.Managers.EntityManager.EntityManager import EntityManager
from living_squares.Managers.InputManager.InputManager import InputManager

from living_squares.Entities.FoodEntity import FoodEntity
from living_squares.Entities.PlayerEntity import PlayerEntity

from typing import TYPE_CHECKING

from living_squares.Managers.SocketManager.SocketManager import SocketManager

if TYPE_CHECKING:
  from living_squares.Entities.Entity import Entity

class LivingSquaresGame(Game):
  def __init__(self, port: int = 9090) -> None:
    super().__init__()
    self.player: PlayerEntity
    self.previous_time: float = time()

    CollisionManager.run()
    SocketManager.run(port=port)

  def draw(self) -> None:
    super().draw()
    current_time: float = time()
    for entity in EntityManager.get_entities():
      entity.tick(current_time - self.previous_time)
    self.previous_time = current_time

  def prepare(self) -> None:
    super().prepare()

    # set the food count
    food_count: int = 15

    # set the window's event handlers
    self.window.on_draw = self.draw
    self.window.on_key_press = InputManager.handle_press

    # crete the player
    self.player = PlayerEntity(self.window)
    self.player.start()

    # create the food
    for _ in range(food_count):
      food_entity: Entity = FoodEntity(self.window)
      food_entity.start()
