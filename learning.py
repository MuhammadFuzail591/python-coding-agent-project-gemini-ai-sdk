import os

def list_file_content(path):

   abs_path = os.path.abspath(path)
   print(f'abs_path: {abs_path}')

   # List filenames in directory
   files = os.listdir(abs_path)
   print(files)
   
   for content in files:
      full_path = os.path.join(abs_path, content)
      file_size = os.path.getsize(full_path)
      is_dir = os.path.isdir(full_path)
      print(f'{content} size = {file_size} bytes, is_dir={is_dir}')


def is_within(working_dir, target_dir = "."):
   abs_working = os.path.abspath(working_dir)

   
   abs_target = os.path.abspath(os.path.join(working_dir, target_dir))


   if not os.path.isdir(abs_target):
      return f'Error: "{target_dir}" is not a directory'
   elif not abs_target.startswith(abs_working + os.sep):
      return f'Error: "{target_dir}" is not in the working directory'
   else:
      return f'Ok done'


# print(is_within("calculator","key"))
# print(is_within("calculator","pkg"))
# print(is_within("calculator","../"))

# list_file_content("calculator")