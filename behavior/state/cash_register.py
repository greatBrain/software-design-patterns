from abc import ABC, abstractmethod

# State interface
class CashState(ABC):
      @abstractmethod
      def handle(self, context):
          ...
      
      @abstractmethod
      def next_state(self, context):
          ...
    
      @abstractmethod
      def previous_state(self, context):
          ...

      @abstractmethod
      def get_state_name(self):
          ...

# Context
class CashRegister:
      def __init__(self, init_state: CashState)->None:
          self._state = init_state

      def set_state(self, state: CashState)-> None:
          print("changing to state {}".format(state.get_state_name()))

      def handle(self):
          self._state.handle(self)

      def next_state(self):
          self._state.next_state(self)

      def previous_state(self):
          self._state.previous_state(self)

      def get_current_state(self):
          return self._state.get_state_name()

# Concrete implementations:
# Estado: Escaneando Productos
class ScanningProducts(CashState):
    def handle(self, context):
        print("Escaneando productos...")

    def next_state(self, context):
        context.set_state(WaitingForPayment())

    def previous_state(self, context):
        print("No hay estado anterior.")

    def get_state_name(self):
        return "Escaneando Productos"

# Estado: Esperando Pago
class WaitingForPayment(CashState):
    def handle(self, context):
        print("Esperando pago del cliente...")

    def next_state(self, context):
        context.set_state(ProcessingPayment())

    def previous_state(self, context):
        context.set_state(ScanningProducts())

    def get_state_name(self):
        return "Esperando Pago"

# Estado: Procesando Pago
class ProcessingPayment(CashState):
    def handle(self, context):
        print("Procesando el pago...")

    def next_state(self, context):
        context.set_state(PrintingReceipt())

    def previous_state(self, context):
        context.set_state(WaitingForPayment())

    def get_state_name(self):
        return "Procesando Pago"

# Estado: Imprimiendo Recibo
class PrintingReceipt(CashState):
    def handle(self, context):
        print("Imprimiendo recibo...")

    def next_state(self, context):
        print("Fin del proceso. Volviendo a estado inicial.")
        context.set_state(ScanningProducts())

    def previous_state(self, context):
        context.set_state(ProcessingPayment())

    def get_state_name(self):
        return "Imprimiendo Recibo"


# Simulación del flujo de estados
def main():
    caja = CashRegister(ScanningProducts())
    
    print(f"Estado inicial: {caja.get_current_state()}")
    caja.handle()
    
    caja.next_state()
    caja.handle()
    
    caja.next_state()
    caja.handle()
    
    caja.next_state()
    caja.handle()
    
    caja.next_state()
    caja.handle()

if __name__ == "__main__":
    main()
