
from functions.get_file_content import get_file_content

def main():

   main_res = get_file_content("calculator","main.py")
   pkg_res = get_file_content("calculator","pkg/calculator.py")
   bin_res = get_file_content("calculator","/bin/cat")
   does_res = get_file_content("calculator","pkg/does_not_exist.py")

   print(main_res)
   print(pkg_res)
   print(bin_res)
   print(does_res)

main()