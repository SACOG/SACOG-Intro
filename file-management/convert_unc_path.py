"""
Name: convert_unc_path.py
Purpose: checks if a path is a UNC path. If it is, it will assign it an unused drive name.
    This is necessary for some Voyager scripts, that do not like UNC paths specified for scripts.


Author: Darren Conly
Last Updated: Jun 2023
Updated by: 
Copyright:   (c) SACOG
Python Version: 3.x
""" 
import re
from pathlib import Path
from collections import namedtuple
import win32api

def map_drive(in_path):
    # future, aspiration thing to add--automatically map a UNC path to a letter drive
    # because voyager scripts require mapping to letter drive


    pathobj = Path(in_path)
    if pathobj.parts[0][0] == '\\': # if input drive is UNC path, map it to an unused letter drive
        parts = list(pathobj.parts)
        drive_url = parts[0]
        drive_url = re.findall('(.*)\\\\', drive_url)[0] # remove trailing '\\' after drive letter in unc
        all_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        used_letters = win32api.GetLogicalDriveStrings().split(':\\\x00')
        map_to_letter = [l for l in all_letters if l not in used_letters][0] # get first letter avaialble that's not already mapped to a drive
        new_drive_name = f"{map_to_letter}:\\"
        parts[0] = new_drive_name # replace UNC drive name with mapped letter drive name
        new_path = Path(*parts)

        # return an object that allows user to map the drive, then unmap the drive once finished so the letter is once again freed up
        driveMap = namedtuple("driveMapCmd", "mapdrive mappedpath unmapdrive")
        cmd_map_drive = f'net use {map_to_letter}: {drive_url}'
        cmd_unmap_drive = f'net use {map_to_letter}: /del'
        result = driveMap(cmd_map_drive, new_path, cmd_unmap_drive)

        # import pdb; pdb.set_trace()
        # import subprocess
        # subprocess.call(cmd_unmap_drive)
        # subprocess.call(cmd_map_drive)
    else:
        result = None
    
    return result


if __name__ == '__main__':
    result = map_drive(r'\\Win10-model-3\d\SACSIM23\PEP_Testing\Baseline\run_2020nets2035LU')
    print(result)