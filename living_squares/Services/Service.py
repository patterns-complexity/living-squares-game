from queue import Queue
from living_squares.Interfaces.IQueuable import IQueueable
from living_squares.Interfaces.IServing import IServing

class Service(IServing):
  def __init__(self, queue: Queue[IQueueable] = Queue()):
    self.queue = queue
    pass
