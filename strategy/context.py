from strategy.duck_strategy import DuckStrategy


class Context:
    def __init__(self) -> None:
        self._duck_strategy = None

    @property
    def duck_strategy(self) -> DuckStrategy:
        return self._duck_strategy

    @duck_strategy.setter
    def duck_strategy(self, duck_strategy: DuckStrategy) -> None:
        self._duck_strategy = duck_strategy

    def do_some_business_logic(self) -> None:
        self._duck_strategy.say_hello()
