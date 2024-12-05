from pathlib import Path
import json


# File validation:
def file_exists(_file:str)->bool:
    _file_path = Path(_file)    
    return True if _file_path.is_file() else False       


def get_file_type(_file:str)->str:
    _file_path = Path(_file)
    _file_type = _file_path.suffix.lstrip('.')
    
    if not _file_type:
       raise ValueError("The file {} does not have a valid extension.".format(_file))   
    return _file_type


def save_file(new_file:str, file_type:str) -> bool:    
    _file = Path(new_file)  #Path object with the file
    destiny_dir = get_directory(file_type) # Name says it all
    _file.rename(destiny_dir / _file.name) # Removes the file, created in the program namespace, to the desired dir       
    
       
def get_directory(file_type:str) -> str:    
    dir_name:str = "{}_files".format(file_type)    
    dir_path = Path(dir_name)
    
    if not dir_path.exists():
       dir_path.mkdir(parents=True, exist_ok=True)
       return dir_path
    
    return None


def get_json_data(_file:str) -> json:
    
    # To normalize the  json file before convert to csv
    with open(_file, "r") as jf:
         j_data = json.load(jf)   
    return j_data