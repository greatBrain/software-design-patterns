from abc import ABC, ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):      
      @abstractstaticmethod
      def person_method():
          """ Interface Method implemented by clients"""


class Student(IPerson):
      def __init__(self):
          self.name = "Student name"
       
      def person_method(self):
          print("Student created")

class Teacher(IPerson):
      def __init__(self):
          self.name = "Teacher name"
         
      def person_method(self):
          print("Teacher created")


class Child(IPerson):
      def __init__(self):
          self.name = "Child name"
        
      def person_method(self):
          print("Child created")


class PersonFactory:

      @staticmethod 
      def create_person(person_type):
          _class_objects = {
             "student": Student(), 
             "teacher": Teacher(),
             "child": Child()
          }

          person_instance = _class_objects.get(person_type.lower())

          if person_instance is None:
             raise ValueError("Person type doesn't exitst!")
          return person_instance


if __name__ == "__main__":
   person_choice = input("Write the person type you want to create:\n")
   person = PersonFactory.create_person(person_choice)    
   person.person_method()
