import argparse
import tabulate
import csv
import os

DIR = os.getcwd() + '\\data'
STORAGE = {}

def get_data_from_csv(path: str):
    try:
        file = csv.reader(open(path, 'r'))
        return file
    except Exception as exc:
        return [{'status': 'Error', 'message': exc}]

def upload_data_to_csv(new_path, data):
    pass

def calculating_average_gdp(file):
    global STORAGE

    for line in file:
        print(line)

        if 'country' in line:
            continue
        if line[0] not in STORAGE:
            count = 1
            STORAGE[line[0]] = [int(line[2]), count]
        elif line[0] in STORAGE:
            STORAGE[line[0]][0] += int(line[2])
            STORAGE[line[0]][1] += 1

    return STORAGE

filename = 'economic1.csv'
output_filename = 'average-gdp'

file = get_data_from_csv(os.path.join(DIR, filename))
print(file)
result = calculating_average_gdp(file)
print(result)



if __name__ == '__main__':
    print(DIR)