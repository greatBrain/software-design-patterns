from converter_base import IConverter
import csv
import json
from utils.helpers import Helper

''' CSV to JSON format converter  '''


class Csv_Converter(IConverter):

    def convert(self, _file:str) -> bool:
        data_from_csv = self._read_csv_conten(_file)
        json_file = 'converted.json'        

        helper = Helper()        

        try:
            with open(json_file, 'w', encoding='utf-8') as jsonf:
                jsonf.write(json.dumps(data_from_csv, indent=4))  
            helper.save()   

        except Exception as e:
            raise e
        
        finally:
            # Erase the helper objetc instance
            del helper


    def _read_csv_content(self, csv_file):
        csv_file
        data = {}

        with open(csv_file, encoding='utf-8') as csvf:
             csvReader = csv.DictReader(csvf)

             for rows in csvReader:
                 p_key = rows['ID']
                 data[p_key] = rows                
             return data