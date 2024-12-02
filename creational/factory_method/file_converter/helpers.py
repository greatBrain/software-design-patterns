from pathlib import Path
import csv
import json

# File validation:
def file_exists(_file:str)->bool:
    _file_path = Path(_file)    
    return True if _file_path.is_file() else False       


def get_file_type(_file:str)->str:
    _file_path = Path(_file)
    _file_type = _file_path.suffix.lstrip('.')
    return _file_type


# Converts csv file into a dict
def csv_to_dict(file_path)->dict:
    data = {}

    with open(file_path) as csvf:
        csv_reader = csv.DictReader(csvf)
        

# Converts csv dict into a json
def csv_data_to_json(file_path)->json:
    pass


# If not exists, create new dir for saving the converted files.
def create_new_file_dir()->None:
    pass


def save_new_file()->True:
    pass
