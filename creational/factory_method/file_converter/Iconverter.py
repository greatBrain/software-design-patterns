from abc import ABCMeta, abstractmethod

class IConverter(metaclass=ABCMeta):
      
      @abstractmethod
      def convert(self, _file:str):
          """ To be implemented """
          pass