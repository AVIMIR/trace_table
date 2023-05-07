import csv
import re


func_print_to_string = '''
import csv
table = [[';'.join(["Номер операции", *vars_dict.keys()]).strip()]]
def print_to_string(*args):
    res_str = ''
    for object in args:
        if type(object) != str:
            object = str(object)

        res_str += ' ' + object

    return res_str
'''
func_table_row_print = '''
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
'''

code = '''
import math
x = float(input("Введите значине X"))
y = math.sin(math.atan(x))
print(y)

d = float(input("Введите значине  точки y"))
g = float(input("Введите значине точки X"))

if d<= g+1 and d<= -g+1 and g>=0:
    print("True")
else:
    print("False")
'''

output = 'Output'
pr_print = 'print'

all_objects_in_code = set()
code_lines = code.split("\n")
new_code_lines = []

for index, line in enumerate(code_lines):
    new_code_lines.append(line)
    var = re.findall(r'[\w]+\s{,1}[\+\-\/\%\*]*=', line)
    print_call = re.findall(r'print\(.*\)', line)

    if print_call:
        var = None

    if var:
        var = re.findall(r'\w+', var[0])[0]
        all_objects_in_code.add(var)
        print(var)
        if index > 0:
            gap = re.findall(r'\s*', code_lines[index])[0]
            new_code_lines.append(gap + 'i_for_table = table_row_print(vars_dict.copy(), {' +    f'"{var}": {var}'   +   '}, i_for_table)\n')

    if print_call:
        content_call = re.findall(r'\(.*\)', print_call[0])[0]
        content_call = re.sub(r'\((.*)\)', r"\1", content_call)
        print(f'print({content_call})')
        if index > 0:
            gap = re.findall(r'\s*', code_lines[index])[0]
            new_code_lines.append(gap + 'i_for_table = table_row_print(vars_dict.copy(), {' +    f'"Вывод": print_to_string({content_call})'   +   '}, i_for_table)\n')


new_code = '\n'.join(new_code_lines)

all_objects_in_code = sorted(all_objects_in_code)
vars_dict = {var: '___' for var in all_objects_in_code}
vars_dict['Вывод'] = '___'
vars_dict = f'vars_dict = {vars_dict}'

new_code_end = '''
print(table)

with open("self_table.csv", "w", newline='') as table_file:
    writer = csv.writer(table_file)
    writer.writerows(table)

'''

funcs = func_print_to_string + func_table_row_print
with open("traceTable.py", "w", encoding='utf-8') as file:
    file.write(vars_dict + funcs + new_code + new_code_end)
    print()
print(code_lines)
print(all_objects_in_code)
