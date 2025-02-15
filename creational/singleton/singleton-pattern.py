# Singleton pattern example

class Singleton(object):
      _instance = None

      def __new__(cls):
          if cls._instance is None:
             cls._instance = super(Singleton, cls).__new__(cls)
          return cls._instance

      def get_data(self):
          return "{data:data}"

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)
