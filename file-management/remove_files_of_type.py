"""
Name: remove_files_of_type.py
Purpose: 
    Remove all files with user-specified extension from user-specified folder with option for
    recursion (deleting from all subfolders as well).

Author: Darren Conly
Last Updated: Sep 2022
Updated by: 
Copyright:   (c) SACOG
Python Version: 3.x
"""
from pathlib import Path
import os, sys

def delete_files_of_type(folder, file_ext, recursive_delete):
    path = Path(folder)
    
    # choose if you only want to delete files of specified type within 
    # specified folder, or if you want to also delete in all subfolders
    pathglob = path.rglob("*") if recursive_delete else path.glob("*")

    print("You are about to delete the following files:")
    delcnt = 0
    bytes_consumed = 0
    files_to_delete = []
    for p in pathglob: 
        sub_p = Path(p)
        ftype = sub_p.suffix
        if ftype == file_ext:
            print(f"\t{sub_p}")
            delcnt += 1
            fsize_bytes = sub_p.stat().st_size
            bytes_consumed += fsize_bytes
            files_to_delete.append(sub_p)

    print(f"{delcnt} {file_ext} files found consume {bytes_consumed / 1_000_000}MB of space.")

    finish_delete = input(f"Do you wish to eliminate these {delcnt} files (enter y/n)? ")
    if finish_delete.lower() == 'y':
        for f in files_to_delete: 
            ftype = f.suffix
            os.remove(f)
            print(f"deleted {f}")
    else:
        print("Operation aborted by user.")
        sys.exit()


if __name__ == '__main__':

    folderpath = input('Enter top folder name:')
    file_type = input('Enter file type you wish to delete (e.g. .rte, include leading period). WARNING: This script will delete ALL files of this type in ALL subfolders: ')
    recursion = input('Do you want to delete these file types in all subfolders (y = yes, n = only delete in earlier-specified folder)? ')

    recursion_dict = {'false':False, 'no':False, 'n':False, 'yes':True, 'y':True, 'true':True}

    delete_files_of_type(folderpath, file_type, recursive_delete=recursion_dict[recursion.lower()])



    """
    more on 'globbing':
    imagine directory 'dir' with 3 files: 't1.txt', '2_t1.txt', 't2.txt'
    running [i for i in dir.glob('*t1.txt')] will return ['t1.txt', '2_t1.txt']
    running .rglob means "recursive glob" and will match pattern in all subfolders
    
    """