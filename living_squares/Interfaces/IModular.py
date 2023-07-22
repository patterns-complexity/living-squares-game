from abc import ABC, abstractmethod

from living_squares.Modules.Module import Module

class IModular():
  @abstractmethod
  def add_module(self, module: Module) -> None:
    pass

  @abstractmethod
  def remove_module(self, id: str) -> None:
    pass

  @abstractmethod
  def list_modules(self) -> dict[str, Module]:
    pass

  @abstractmethod
  def module(self, name: str) -> Module:
    pass

  @abstractmethod
  def main(self) -> None:
    pass