#       2021 © Zoda
#Bütün hakları Zoda'ya aittir
import os
from colorama import init
from termcolor import colored
init()
class DirectoryNotFoundError(Exception):
    def __init__(self, salary, message="DirectoryNotFound"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return colored(f'Directory Name: {self.salary}', 'red')

def copy(file_name, output_dir):
    if os.path.exists(file_name):
        if os.path.exists(output_dir):

            #output file code
            output_code = output_dir + '\\' + file_name
            if os.path.exists(output_code):
                raise FileExistsError(colored(f"{output_code} already exits!", "red"))
            else:
                file = open(file_name, "r").read()
                with open(f"{output_code}", "w") as output:
                    output.write(file)

        else:
            raise DirectoryNotFoundError(output_dir)
    else:
        print(f"FileNotFound: {file_name}")