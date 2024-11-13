from abc import ABCMeta, ABC, abstractstaticmethod

class INotification(metaclass=ABCMeta):
      
      @abstractstaticmethod
      def send(self, message:str)->None:
          ''' To be implemented by clients '''
          pass
