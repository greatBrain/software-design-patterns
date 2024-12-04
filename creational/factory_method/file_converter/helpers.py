from pathlib import Path


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
    directory = Path(file_type)    
    directory.mkdir(parents=True, exist_ok=True)
       
