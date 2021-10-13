#!/usr/bin/python

import math
import sys

Data = []
X = []


def ReadCSV():
    FileName = sys.argv[1]
    f = open(FileName)
    for line in f:
        Data.append(line)
    f.close()
    for line in Data:
        f = line.strip().split(",")
        X.append(f)
    return X


X = ReadCSV()
