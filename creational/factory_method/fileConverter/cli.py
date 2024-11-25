from pathlib import Path
import click
from converters.converter_factory import ConverterFactory

@click.command()
@click.option('-f', '--file', type=click.Path(exists=True), help="The path of the file you want to convert.")
@click.option('--convert', is_flag=True, help="The file must be converted.")
def run(file, convert)->None:   

    try:
      if convert:
         def _get_file():
            file_abs_path = Path(file).resolve()

            if not file_abs_path:
               raise ValueError("File not found")         
            file_path_and_extension = (file_abs_path.parent, Path(file_abs_path).suffix.lstrip('.')) 
            ConverterFactory.create_converter(file_path_and_extension)

            
    except:
        raise ValueError("No file or convertion option found")
    


''' Example of running this command:  python main.py --convert --file /path/to/file.ext  '''