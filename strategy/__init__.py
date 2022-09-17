from strategy.context import Context
from strategy.home_duck import HomeDuck
from strategy.mallard_duck import MallardDuck

if __name__ == "__main__":
    context = Context()

    context.duck_strategy = MallardDuck()
    print("Client: Strategy is create MallardDuck")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is create HomeDuck")
    context.duck_strategy = HomeDuck()
    context.do_some_business_logic()
