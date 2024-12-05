import csv
import json
from Iconverter import IConverter
import helpers

class CSVConverter(IConverter):      
      '''converter method implementation. Converts to json format.'''
      def convert(self, csv_file:str):          
          data = []
          json_file = 'converted.json'          
          
          try:
              with open(csv_file, encoding='utf-8') as csvf:
                   csv_reader = csv.DictReader(csvf)
                   data = [row for row in csv_reader]

              with open(json_file, 'w') as jf:
                   json.dump(data, jf)                                    
              helpers.save_file(json_file, 'json')
                
          except FileNotFoundError:
                print("Error: The file {} was not found.".format(csv_file))
          
          except Exception as e:
                print("An unexpected error occurred: {}".format(e))


            
            
class JSONConverter(IConverter):
      '''converter method implementation. Converts to csv format.'''
      def convert(self, _file:str):
          pass