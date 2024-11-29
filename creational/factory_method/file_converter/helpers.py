from pathlib import Path
import csv
import json

# File validation:
def file_exists(file_path:str)->bool:
    if not file_path:
       return False 
    return True


def get_file_ext(file_path:str)->str:
    pass


# Converts csv file into a dict
def csv_to_dict(file_path)->dict:
    pass


# Converts csv dict into a json
def csv_data_to_json(file_path)->json:
    pass


# If not exists, create new dir for saving the converted files.
def create_new_file_dir()->None:
    pass


def save_new_file()->True:
    pass
