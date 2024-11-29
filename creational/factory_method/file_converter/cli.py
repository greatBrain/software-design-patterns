import click
from helpers import file_exists

@click.command()
@click.argument('filename')
@click.option("-c", "--convert", type=str, prompt='insert the csv file name', help='csv file path')
def run():

    def convert_file():
        if not file_exists(filename):
           @click.echo("This file or path does not exist.") 
        