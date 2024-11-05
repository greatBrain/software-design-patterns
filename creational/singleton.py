# SINGLETON PATTERN
#
# Ensure that a class has only one instance and provides a global point of access to it.

# The singleton design pattern is used in real-world projects to control access to shared resources, 
# manage state, and coordinate system-wide actions.
#
# Clients (instances) may not even realize that they’re working with the same object all the time.
#
# Lesson chapter: https://refactoring.guru/design-patterns/singleton
#
# For this purpose, i'll be using metaclass, knowing that there are other methods for doing this (decorator, base class and so on)
#

''' WARNING: This pattern its a little problematic. It violates some SOLID principles.'''

class SingletonMeta(type):
      
      _instances = {}

        
      def __call__(cls, *args, **kwargs):
          
          if cls not in cls._instances:
             instance = super().__call__(*args, **kwargs)
             cls._instances[cls] = instance
          
          return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
