#!/usr/local/bin/python

import sys
sys.path.append('./')
import anonymize_dicom

param = sys.argv


anonymize_dicom.anonymize_file(param[1], param[2]);
