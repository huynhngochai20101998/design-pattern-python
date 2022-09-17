from abc import ABC, abstractmethod


class DuckStrategy(ABC):
    @abstractmethod
    def say_hello(self):
        pass
