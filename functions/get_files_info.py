import os
from google.genai import types


def get_files_info(working_directory, directory = "."):

   abs_working_dir = os.path.abspath(working_directory)
   
   abs_path = os.path.abspath(os.path.join(working_directory, directory))

   print(f'Result for "{directory}" directory')
   if not os.path.isdir(abs_path):
      return f'Error: "{directory}" is not a directory'

   if not abs_path.startswith(abs_working_dir):
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

   contents = os.listdir(abs_path)

   result = ""

   for content in contents:
      content_path = os.path.join(abs_path,content)
      file_size = os.path.getsize(content_path)
      is_dir = os.path.isdir(content_path)
      
      result += f'- {content}: file_size={file_size} bytes, is_dir={is_dir}\n'

   return result


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)