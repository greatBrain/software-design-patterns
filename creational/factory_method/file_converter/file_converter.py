import csv
import json
import pandas as pd
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
      def convert(self, json_file:str):        
          csv_file = "converted.csv"  

          try:
             json_data = pd.read_json(json_file)
             json_data.to_csv(csv_file, index=False)
             helpers.save_file(csv_file, 'csv')
                
          except FileNotFoundError:
                print("Error: The file {} was not found.".format(json_file))
          
          except Exception as e:
                print("An unexpected error occurred: {}".format(e))
