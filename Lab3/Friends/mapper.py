#!/usr/bin/python
# -*-coding:utf-8 -*

# import sys because we need to read and write data to STDIN and STDOUT
import sys
  
# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(', ')

    print ('%s\t%s' % (words[0], 1))