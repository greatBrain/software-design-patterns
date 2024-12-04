import click
import helpers
from converter_factory import Converter_Factory

@click.command()
@click.option('--convert', 'filename', required=True, help='file we want to convert.')
def run(filename):

    if not filename:   
       click.echo("wrong filename or missing option.")

    def _convert_file():
        if not helpers.file_exists(filename):
           click.echo("This file or path does not exist") 
           return False           
           
        _file_type = helpers.get_file_type(filename) # get the file type (extension)           
        converter = Converter_Factory.get_instance(_file_type)
                
    _convert_file()
           