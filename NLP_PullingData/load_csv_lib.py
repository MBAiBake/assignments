# Netid: tmb9978 and Jake Reiner
# Change the line above 

import csv

def load_csv(file_name):
    dict = {}
    keys = []
    values = []
    with open(file_name, "r") as input:
        testpop = csv.reader(input)
        next(testpop)
        testpop = list(testpop)
        for row in testpop:
            dict[str.lower(row[0])] = [row[4], row[2]]
    for i in range(len(keys)):
        dict[keys[i]] = values[i]
    return dict



