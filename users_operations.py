# imports
## builtin

# installed lib.

# user_defined modules
from read_save_data import  save_data_to_file, read_line_by_line


##I need to save the user to the file then ,,,  display it
user_name = input("Please enter your name: ")
password = input("Please enter your password: ")

data_to_save = f"{user_name}:{password}\n"

saved = save_data_to_file("users.txt", data_to_save)
print(saved)

lines = read_line_by_line("users.txt")

