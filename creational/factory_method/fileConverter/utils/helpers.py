from pathlib import Path
import shutil

class Helper:
      def __init__(self):
          self.file_path_and_extension = ''

      
      def get_file_name_and_extension(self, _file)->tuple:          
         file_abs_path = Path(_file).resolve()

         if not file_abs_path:
            raise ValueError("File not found")
         
         self.file_path_and_extension = (file_abs_path.parent, Path(file_abs_path).suffix.lstrip('.'))       
         file_ext = self.file_path_and_extension[1]
         self.dir_created(file_ext)


      def dir_created(self, file_type:str='')->bool:
          new_dir_name = str(file_type + '_files')
          new_dir = Path(new_dir_name)

          try:
            new_dir.mkdir(parents=True, exist_ok=True)
            return True 
          except ValueError as e:
            raise ("Directory could not be created", e)


      def save(self, src_path:str='', dst_path:str='')->bool:
         
          if not self.dir_created():
             return False    
          else:
             shutil.move(src_path, dst_path)
             return True  

