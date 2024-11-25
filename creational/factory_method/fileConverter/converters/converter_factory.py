from csv_converter import Csv_Converter
from image_converter import Image_Converter
from json_converter import Json_Converter
from pdf_converter import Pdf_Converter
from utils import helpers

class ConverterFactory:
      
      @staticmethod
      def create_converter(file_properties:tuple) -> object:
          
          # Csv converter: CSV files  TO JSON format
          # Json converter: JSON files  TO CSV format
          # Image converter: png,jpg files TO webp format
          # Pdf converter: docx files TO pdf format

          instances_map = {
             "csv":Csv_Converter,
             "json":Json_Converter,
             "jpg":Image_Converter,
             "png":Image_Converter,             
             "docx":Pdf_Converter
          }

          file_path = file_properties[0]
          file_type = file_properties[1]

          converter_instance = instances_map.get(file_type.lower())

          if not converter_instance:
             raise ValueError("Error in file type {}. Try again.".format(file_type))
          return converter_instance()          
