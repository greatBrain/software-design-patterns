from pathlib import Path
import shutil
import click

# We get the file as a command line argument and its path and extension.
@click.command()
@click.argument('file', type=click.Path(exists=True))
def get_file(file)->tuple:          
    file_abs_path = Path(file).resolve()

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


def save(old_path:str='', new_path:str='')->bool:
    
    if dir_created():
       pass

