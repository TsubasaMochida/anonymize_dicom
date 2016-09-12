#!/usr/local/bin/python

import sys
sys.path.append('./')
import anonymize_dicom

param = sys.argv

try:
    anonymize_dicom.anonymize_file(param[1], param[2]);
    sys.stdout.write('Success')
except:
    sys.stderr.write('Error occurred!')
