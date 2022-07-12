#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:22:25 2019

@author: darrenconly

https://docs.python.org/3/library/traceback.html
https://www.geeksforgeeks.org/traceback-in-python/
"""

import sys

import traceback as tb
    
#============Z's traceback function=====================
        
def trace_z_ye():
    import traceback, inspect
    import pdb; pdb.set_trace()
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    # script name + line number
    line = tbinfo.split(", ")[1]
    filename = inspect.getfile(inspect.currentframe())
    # Get Python syntax error
    synerror = traceback.format_exc().splitlines()[-1]
    return line, filename, synerror #return line number, name of file with error line, and type of error

#implementing Z's traceback function
for i in [1,2,3,0,4,'a',9]:
    try:
        print(1/i)
    except:
        out_error_info = trace_z_ye()
        print(out_error_info)