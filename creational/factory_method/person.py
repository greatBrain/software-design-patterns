from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):      
      @abstractstaticmethod
      def get_person(self):
          pass     


class Haitian(IPerson):      
      def __init__(self):
          self.name = "Name"

      def get_person(self):
          print("Haitian created")


class Australian(IPerson):
        
      def __init__(self):
          self.name = "Name"

      def get_person(self):
          print("Australian person created")


class PersonFactory:
      
      person_factory_map = {
        "haitian":Haitian,
        "australian":Australian
      }
      
      @staticmethod
      def get_person(person_type):

      
      
      
