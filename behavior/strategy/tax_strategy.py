from abc import ABC, abstractmethod

class Tax_Strategy(ABC):
      @abstractmethod 
      def calculate(self, amount: float)-> float:  
          pass


class IVAStrategy(Tax_Strategy):
      def calculate(self, amount:float)->float:
          return (amount * 0.16)

class ISRStrategy(Tax_Strategy):
      def calculate(self, amount:float)->float:
          return (amount * 0.30)


# Context
class TaxCalculator:
      def __init__(self, strategy:Tax_Strategy):
          self.__strategy = strategy

      def set_strategy(self, strategy:Tax_Strategy):
          self.__strategy = strategy

      def calculate(self, amounts:list[float])-> list[float]:
          taxes = [amount for amount in amounts self.__strategy.calculate(amount)]    
          return taxes
          

amounts = [100,18,24,320]
iva_strategy = IVAStrategy()
isr_strategy = ISRStrategy()
tax_calculator = TaxCalculator(iva_strategy)

print(tax_calculator.calculate(amounts))

tax_calculator.set_strategy(isr_strategy)

print(tax_calculator.calculate(amounts))

