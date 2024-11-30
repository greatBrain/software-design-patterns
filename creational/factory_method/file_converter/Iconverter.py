from abc import ABCMeta, abstractmethod

class IConverter(metaclass=ABCMeta):
      
      @staticmethod
      @abstractmethod
      def convert(self, _file):
          """ To be implemented """