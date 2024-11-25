from pathlib import Path
import shutil

class Helper:

      def save(self, file_type:str='txt', src_path:str='')->bool:
         
          try:
              dest_dir_name = self.dir_created(file_type)
              shutil.move(src_path, dest_dir_name)
              return True  
          except:
              raise Exception


      def dir_created(self, file_type:str='')->str:
          new_dir_name = str(file_type + '_files')
          new_dir = Path(new_dir_name)

          try:
            new_dir.mkdir(parents=True, exist_ok=True)
            return new_dir 
          except ValueError as e:
            raise ("Directory could not be created", e)


     
