from uuid import UUID, uuid4

from living_squares.Managers.EntityManager.EntityManager import EntityManager

from living_squares.Interfaces.IModular import IModular

from living_squares.Modules.Module import Module

class Entity(IModular):
  def __init__(self) -> None:
    self.id: UUID = uuid4()
    self.modules: dict[str, Module] = {}

  def __del__(self) -> None:
    EntityManager.unregister_entity(self)

  def add_module(self, module: Module) -> None:
    self.modules[module.name] = module

  def remove_module(self, id: str) -> None:
    del self.modules[id]

  def list_modules(self) -> dict[str, Module]:
    return self.modules

  def module(self, name: str) -> Module:
    return self.modules[name]

  def destroy(self) -> None:
    del self

  def setup(self) -> None:
    pass

  def _setup_modules(self) -> None:
    for module in self.modules.values():
      module.register_as_observer()
    pass

  def start(self) -> None:
    self.setup()
    self._setup_modules()
    EntityManager.register_entity(self)

  def tick(self) -> None:
    for module in self.modules.values():
      module.tick()
