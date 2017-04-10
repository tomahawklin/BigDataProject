#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)
#valid_list = ['BRONX','BROOKLYN','MANHATTAN','QUEENS','STATEN ISLAND']
for entry in reader:
    #if len(entry) == 22:
    Y_COORD_CD = str(entry[20])
    if Y_COORD_CD == '' or Y_COORD_CD is None:#in valid_list:
        label = 'NULL'
        Y_COORD_CD = 'NULL'
    else:
        label = 'VALID'
    print('%s\t%s,coordinate,%s' % (Y_COORD_CD, get_type(Y_COORD_CD), label))
    
