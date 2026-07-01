# function needs to copy all contents from src -> destination
# 1-> check if destination folder exists
# 2-> delete all contents from the destination folder
# 3-> copy all files and subdirectories from src into destination
import os
import shutil

def copy_fresh_contents(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
    
    # remove all contents from the destination
    remove_contents(dst)

    # copy all files and subdirectories from src into dst
    copy_contents(src, dst)


def remove_contents(path):
    inner_paths = os.listdir(path)
    for inner_path in inner_paths:
        full_path_name = os.path.join(path, inner_path)
        if os.path.isfile(full_path_name):
            os.remove(full_path_name)
        else:
            remove_contents(full_path_name)
            os.rmdir(full_path_name)
            

def copy_contents(src, dst):
    inner_paths = os.listdir(src)
    for inner_path in inner_paths:
        full_path_name = os.path.join(src, inner_path)
        destination_path = os.path.join(dst, inner_path)
        if os.path.isfile(full_path_name):
            shutil.copy(full_path_name, destination_path)
        else:
            os.mkdir(destination_path)
            copy_contents(full_path_name, destination_path)