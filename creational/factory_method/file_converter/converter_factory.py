from file_converter import CSVConverter, JSONConverter

class Converter_Factory:
      
      @staticmethod
      def get_instance(file_type:str)->object:
          instances = {
              'csv':CSVConverter(),
              'json':JSONConverter()
          }          
      
          converter_instance = instances.get(file_type)
          if not converter_instance is  None: return converter_instance