a_file = open("errors_py.py", "r")
list_of_lines = a_file.readlines()
list_of_lines[1] = list_of_lines[1].replace("True", "False")

a_file = open("errors_py.py", "w")
a_file.writelines(list_of_lines)
a_file.close()

    