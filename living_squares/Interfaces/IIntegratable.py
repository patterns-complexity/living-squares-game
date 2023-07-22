from abc import ABC, abstractmethod

class IIntegratable():
  @abstractmethod
  def main(self) -> None:
    pass

  @abstractmethod
  def tick(self) -> None:
    pass