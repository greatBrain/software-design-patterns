import click
import helpers
from converter_factory import Converter_Factory

@click.command()
@click.argument('filename')
@click.option('--convert', help='file we want to convert in.')
def run(filename, convert):
    
    _file = filename
    
    if convert != "default.json":     
       def _convert_file():
           if not helpers.file_exists(_file):
              click.echo("This file or path does not exist") 
              return False           
           
           _file_type = helpers.get_file_type(_file) # get the file type (extension)           
           converter = Converter_Factory.get_instance(_file_type)
           print(converter)           
       _convert_file()
           