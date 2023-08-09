# Write your code here :-)
import os

def find_files(suffix, path):
    files_with_suffix = []
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path) and full_path.endswith(suffix):
            files_with_suffix.append(full_path)
        elif os.path.isdir(full_path):
            files_with_suffix.extend(find_files(suffix, full_path))
    return files_with_suffix

directory_path = "\\Users\\T1898BC\\Documents\\Data structures\\testdir"
suffix_to_find = ".c"
c_files = find_files(suffix_to_find, directory_path)
for file in c_files:
    print(file)
#\subdir1\a.c
#\subdir3\subsubdir1\b.c
#\subdir5\a.c
#\t1.c

directory_path = ""
suffix_to_find = ".c"
c_files = find_files(suffix_to_find, directory_path)
for file in c_files:
    print(file)
#FileNotFoundError: [WinError 3] The system cannot find the path specified: ''

directory_path = "None"
suffix_to_find = ".c"
c_files = find_files(suffix_to_find, directory_path)
for file in c_files:
    print(file)
#FileNotFoundError: [WinError 3] The system cannot find the path specified: 'None'



