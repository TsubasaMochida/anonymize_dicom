#!/usr/local/bin/python
import sys
param = sys.argv

# https://github.com/darcymason/pydicom/blob/26e769b63a12eb3295588961ed22a81643aa9de2/pydicom/misc.py
def is_dicom(file):
    fp = open(file, 'rb')
    preamble = fp.read(0x80)
    magic = fp.read(4)
    if magic == b"DICM":
        return True
    else:
        return False

if is_dicom(param[1]) :
    sys.stdout.write('TRUE')
else :
    sys.stdout.write('FALSE')

