vars_dict = {'d': '___', 'g': '___', 'x': '___', 'y': '___', 'Вывод': '___'}
import csv
table = [[';'.join(["Номер операции", *vars_dict.keys()]).strip()]]
def print_to_string(*args):
    res_str = ''
    for object in args:
        if type(object) != str:
            object = str(object)

        res_str += ' ' + object

    return res_str

def table_row_print(vars_dict_copy, vars_changed, i_for):
    for var_name in vars_changed:
        vars_dict_copy[var_name] = str(vars_changed[var_name])

    content = ';'.join([f'{i_for}', *vars_dict_copy.values()])

    print(f'{i_for:<2d}) {vars_dict_copy.values()}')
    print(content)

    table.append([content])
    i_for += 1

    return i_for

i_for_table = 1

import math
x = float(input("Введите значине X"))
i_for_table = table_row_print(vars_dict.copy(), {"x": x}, i_for_table)

y = math.sin(math.atan(x))
i_for_table = table_row_print(vars_dict.copy(), {"y": y}, i_for_table)

print(y)
i_for_table = table_row_print(vars_dict.copy(), {"Вывод": print_to_string(y)}, i_for_table)


d = float(input("Введите значине  точки y"))
i_for_table = table_row_print(vars_dict.copy(), {"d": d}, i_for_table)

g = float(input("Введите значине точки X"))
i_for_table = table_row_print(vars_dict.copy(), {"g": g}, i_for_table)


if d<= g+1 and d<= -g+1 and g>=0:
    print("True")
    i_for_table = table_row_print(vars_dict.copy(), {"Вывод": print_to_string("True")}, i_for_table)

else:
    print("False")
    i_for_table = table_row_print(vars_dict.copy(), {"Вывод": print_to_string("False")}, i_for_table)


print(table)

with open("self_table.csv", "w", newline='') as table_file:
    writer = csv.writer(table_file)
    writer.writerows(table)

