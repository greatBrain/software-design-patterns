from utils.helpers import Helper
import click

@click.command()
#@click.argument('file', type=click.Path(exists=True))
@click.option('-f', '--file', type=click.Path(exists=True), help="The path of the file you want to convert.")
@click.option('--convert', is_flag=True, help="The file must be converted.")
def run(file, convert)->None:
    helper = Helper()

    try:
        if convert:
           def _get_file_from_argument()-> None:
               helper.get_file_name_and_extension(file)
           _get_file_from_argument()        
    except:
        raise ValueError("No file or convertion option found")
    finally:
        del helper