from pathlib import Path
import click


class Helper:
      def __init__(self):          
         self.file_abs_path = ''

      # Get file from terminal argument
      @click.command()
      @click.argument('file', type=click.Path(exists=True))
      def get_file(self, file)->str:          
          self.file_abs_path = Path(file).resolve()


      # Get file type by extension
      def get_file_type(self)->str:                    
          file_extension = ''

          if not self.file_abs_path:
             print("No file found.")
        
          file_extension = Path.suffix(self.file_abs_path)
          print(file_extension)    

if __name__ == "__main__":
   helpers = Helper()
   helpers.get_file()