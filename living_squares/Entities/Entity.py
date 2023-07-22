from uuid import UUID, uuid4

from living_squares.Managers.EntityManager import EntityManager

from living_squares.Interfaces.IModular import IModular

from living_squares.Modules.Module import Module

class Entity(IModular):
  def __init__(self):
    self.id: UUID = uuid4()
    self.modules: dict[str, Module] = {}
    EntityManager.register_entity(self)

  def __del__(self):
    EntityManager.unregister_entity(self)

  def add_module(self, module: Module) -> None:
    self.modules[module.name] = module

  def remove_module(self, id: str) -> None:
    del self.modules[id]

  def list_modules(self) -> dict[str, Module]:
    return self.modules

  def module(self, name: str) -> Module:
    return self.modules[name]

  def tick(self) -> None:
    for module in self.modules.values():
      module.tick()

  def register(self, entity_list: list['Entity'] | None = None) -> None:
    if entity_list is None:
      return

    entity_list.append(self)