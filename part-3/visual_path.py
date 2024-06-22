import sys
from pathlib import Path
from colorama import Fore

input_value = sys.argv[1]
directory = Path(input_value)
counter = 0

path_list = []

if directory.exists():
    if directory.is_dir() and not directory.is_file():
        for path in directory.iterdir():
            path_list.append(path.parent.name)
            print(f'{Fore.BLUE}{path_list[0]}/{Fore.RESET}')
            break
    else:
        print("You have to choose some folder`s path, not a file, check it and try again")
else:
    print("Seams like chosen directory does not exist, check it and try again")

def dir_counter(path=Path): 
    if path.is_dir():
        global counter
        counter += 1
        print(f'{"\t" * counter}{Fore.BLUE}{path.name}/{Fore.RESET}')
        
        for item in path.iterdir():
            if item.is_dir():
                dir_counter(item)
                
                           
            else:
                counter = counter + 1
                print(f'{"\t" * counter}{Fore.GREEN}{item.name}{Fore.RESET}')
                counter -= 1
        counter -= 1

    else:
        counter += 1
        print(f'{"\t" * counter }{Fore.GREEN}{path.name}{Fore.RESET}')
        counter -= 1

if directory.exists() and directory.is_dir():
    for path in directory.iterdir():
        dir_counter(path)
else:
    pass

# TO TEST: copy&paste to the terminal: python3 visual_path.py part-2   