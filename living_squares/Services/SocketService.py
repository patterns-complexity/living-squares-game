import socket

from typing import Any, Callable
from living_squares.Services.Service import Service

class SocketService(Service):
  def __init__(self, port: int) -> None:
    super().__init__()
    self.port: int = port
    pass

  def run(self, callback: Callable[[Any], None]) -> None:
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', self.port))
        s.listen()
        conn, addr = s.accept()
        with conn:
          while True:
            data = conn.recv(1024)
            if not data:
              break
            callback(data)
    except Exception as e:
      callback(e)
      pass

