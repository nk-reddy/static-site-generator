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
    if len(inner_paths) == 0:
        return
    for path in inner_paths:
        if os.path.isfile(path):
            os.remove(path)
        else:
            remove_contents(path)
            os.rmdir(path)


def copy_contents(src, dst):
    inner_paths = os.listdir(src)
    if len(inner_paths) == 0:
        return 
    
    # need to get the extension post the src to be able to put into dst
    

    for path in inner_paths:
        if os.path.isfile(path):
            shutil.copy(path, dst)