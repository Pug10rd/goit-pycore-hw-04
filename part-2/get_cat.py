import re
from pathlib import Path

def get_cats_info(path):
    cats_list = []
    path_param = Path(path)
    if path_param.exists() and path_param.is_file():
        with open(path, 'r') as fh:
            lines_list = fh.readlines()
            pattern = r"\,"
            for i in lines_list:
                save = re.split(pattern, i)
                cat_profile = {
                    "id": f"{save[0]}",
                    "name": f'{save[1]}',
                    "age": f'{int(save[2])}',
                }
                cats_list.append(cat_profile)
        return cats_list
    else:
        print("Please, check the path and try again")

#test part below
#  | 
# \|/
#  v

cats_info = get_cats_info("part-2/cats.txt")

print(cats_info)
