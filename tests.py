
from functions.get_file_content import get_file_content
from functions.write_file import write_file
def main():

   main_res = write_file("calculator","lorem.txt", "wait, this isn't lorem ipsum")
   pkg_res = write_file("calculator","pkg/morelorem.txt", "lorem ipsum dolor sit amet")

   does_res = write_file("calculator","tmp/temp.txt","this should not be allowed")

   print(main_res)
   print(pkg_res)
   print(does_res)

main()