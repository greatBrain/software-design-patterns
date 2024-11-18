from abc import ABCMeta, ABC, abstractstaticmethod

# Factory base class 
class IConverter(metaclass=ABCMeta):      

      @abstractstaticmethod
      def convert(file_type:str):
          ''' To be implemented by clients '''
          pass
