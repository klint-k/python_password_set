#!/usr/bin/python3
# -*- coding: utf-8 -*-

import getpass
from os import chdir
from os import path
from platform import python_version_tuple

#Variables
global Path
Path = ('/usr/lib/python' +
        python_version_tuple()[0] +
        '.' +
        python_version_tuple()[1] +
        '/passwd.py')

try:
    import passwd
except Exception as e:
    print("This is the first time that this is run for this Python.", e)
    with open(Path, 'w') as file_obj:
        Data = ('#!/usr/bin/python3\n# -*- coding: utf-8 -*-\n\n')
        file_obj.write(Data)


def ask_var(var_name = '', var_data = ''):
    user = getpass.getuser()
    if user == 'root':
        if var_name == '':
            var_name = input("What would you like to use as a variable name?   ")
            if var_name == '':
                return
        try:
            for var_test in dir(passwd):
                if var_test == var_name:
                    with open(Path, 'r') as file_obj0:
                        file_list = file_obj0.readlines()
                    file_obj0.close()
                    with open(Path, 'w') as file_obj:
                        for line in file_list:
                            if not line.startswith(var_name):
                                file_obj.write(line)
                    file_obj0.close()
                    y_n = input('Do you want to keep this variable name? (Y) or N?  ')
                    # cleanup
                    if y_n == '':
                        y_n = 'Y'
                    y_n = y_n.upper()
                    y_n = y_n[0]
                    if y_n == "Y":
                        break
                    elif y_n == 'N':
                        return
                else:
                    pass
        except NameError:
            pass
        if var_data == '':
            var_data = input('What would you like to use as a variable?   ')
            if var_data == '':
                return
        data = var_name + ' = "' + var_data + '"'
        with open(Path, 'a') as file_obj:
            Data = data + '\n'
            file_obj.write(Data)
        file_obj.close()
    else:
        pass


if __name__ == '__main__':
    while True:
        ask_var()
        y_n = input('Do you want to add another variable? (Y) or N?  ')
        # cleanup
        if y_n == '':
            y_n = 'Y'
        y_n = y_n.upper()
        y_n = y_n[0]
        if y_n == "Y":
            pass
        elif y_n == 'N':
            break
    print()
    with open(Path, 'r') as file_obj:
        file_list = file_obj.readlines()
    for K in file_list:
        print(K.rstrip('\n'))
    print()



