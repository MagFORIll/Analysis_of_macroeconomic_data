import argparse
import tabulate
import csv
import os

DIR = os.getcwd() + '\\data'
STORAGE = {}

def get_data_from_csv(path: str):
    try:
        file = csv.DictReader(open(path, 'r'))
        return file
    except Exception as exc:
        return [{'status': 'Error', 'message': exc}]

def upload_data_to_csv(new_path: str):
    with open(new_path, 'w', newline='') as output_file:
        output_file = csv.writer(output_file)
        output_file.writerow(['country','gpd'])
        for line in STORAGE:
            line = [line,STORAGE[line][0]]
            output_file.writerow(line)

def calculating_average_gdp(file):
    global STORAGE

    for row in file:
        if row['country'] not in STORAGE:
            count = 1
            STORAGE[row['country']] = [int(row['gdp']), count]

        elif row['country'] in STORAGE:
            STORAGE[row['country']][0] += int(row['gdp'])
            STORAGE[row['country']][1] += 1


    return STORAGE

filename = ['economic1.csv', 'economic2.csv']
output_filename = 'average-gdp.csv'

for file in filename:
    file = get_data_from_csv(os.path.join(DIR, file))
    calculating_average_gdp(file)



upload_data_to_csv(output_filename)



if __name__ == '__main__':
    print(DIR)