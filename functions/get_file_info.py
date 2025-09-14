import os

def get_files_info(working_directory, directory="."):
   path = os.path.join(working_directory,directory)
   print(path)

get_files_info()