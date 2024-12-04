from file_converter import CSVConverter, JSONConverter

class Converter_Factory:
      @staticmethod
      def get_instance(file_type:str)->object:
          instances = {
              'csv':CSVConverter,
              'json':JSONConverter
          }
          
          converter_instance = instances.get(file_type)
          return converter_instance() if converter_instance is not None else None