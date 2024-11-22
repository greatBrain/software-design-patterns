from pathlib import Path
import shutil

class Helper:
      def __init__(self):
          self.file_path_and_extension = ''

      
      def get_file_name_and_extension(self, _file)->tuple:          
         file_abs_path = Path(_file).resolve()

         if not file_abs_path:
            raise ValueError("File not found")
         
         self.file_path_and_extension = (file_abs_path.parent, Path(file_abs_path).suffix)         
         self.dir_created(self.file_path_and_extension[1])


      def dir_created(self, file_type:str='')->bool:
          new_dir_name = str(file_type)
          new_dir = Path(new_dir_name)

          try:
            new_dir.mkdir(parents=True, exists_ok=True)
            return True 
          except:
            raise Exception("Directory could not be created", Exception)


      def save(self, src_path:str='', dst_path:str='')->bool:
         
          if not self.dir_created():
             return False    
          else:
             shutil.move(src_path, dst_path)
             return True  

