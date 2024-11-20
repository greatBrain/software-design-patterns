from pathlib import Path
import shutil


def get_file_name_and_extension(_file)->tuple:          
    file_abs_path = Path(_file).resolve()

    if not file_abs_path:
       raise ValueError("File not found")
    
    file_path_and_extension = (file_abs_path.parent, Path(file_abs_path).suffix)
    return file_path_and_extension


def dir_created(file_type:str='')->bool:
    new_dir_name = str(file_type)
    new_dir = Path(new_dir_name)

    try:
       new_dir.mkdir(parents=True, exists_ok=True)
       return True 
    except:
       raise Exception("Directory could not be created")


def save(src_path:str='', dst_path:str='')->bool:
    
    if not dir_created():
       return False    
    else:
       shutil.move(src_path, dst_path)
       return True

