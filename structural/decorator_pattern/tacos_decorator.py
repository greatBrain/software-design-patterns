from abc import ABC, abstractmethod

class Taco(ABC):      
      @abstractmethod
      def price(self):
          pass

class BasicTaco(Taco):
      def price(self):
          return 15

class TacoDecorator(Taco):
      def __init__(self, taco: Taco):
          self._taco = taco

      def price(self):
          return self._taco.price()


class DoubleMeatTaco(TacoDecorator):
      def price(self):
          return self._taco.price()+5

class CheeseTaco(TacoDecorator):
      def price(self):
          return self._taco.price()+3



base_taco = BasicTaco()
print(base_taco.price())

meat_taco = DoubleMeatTaco(base_taco)
print(meat_taco.price())

cheese_taco = CheeseTaco(meat_taco)
print(cheese_taco.price())
