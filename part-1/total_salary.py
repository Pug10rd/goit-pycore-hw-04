import re
from pathlib import Path

def total_salary(path):
    path_param = Path(path)
    if path_param.exists() and path_param.is_file():
        sum_salary = 0
        with open(path, 'r') as fh:
            lines_list = fh.readlines()
            pattern = r"\,"
            for i in lines_list:
                save = re.split(pattern, i)
                sum_salary = sum_salary + int(save[1])
                
        total = sum_salary
        average = f'{(sum_salary / len(lines_list)):.0f}'
        return (total, average)
    else:
        print("Please, check the path and try again")

#test part below
#  | 
# \|/
#  v

total, average = total_salary('part-1/test.txt')

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
