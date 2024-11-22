from utils.helpers import Helper
import click

@click.command()
@click.argument('file', type=click.Path(exists=True))
def run(file)->None:
    helper = Helper()

    def _get_file_from_argument()-> None:
        helper.get_file_name_and_extension(file)
    _get_file_from_argument()

    del helper