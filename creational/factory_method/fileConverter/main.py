import click
from utils import helpers

# Gets the file from argument
@click.command()
@click.argument('file', type=click.Path(exists=True))
def get_file_from_argument(file)-> None:
    helpers.get_file_name_and_extension(file)


def run()->None:
    pass

if __name__ == "__main__":
   pass