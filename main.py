import argparse
import csv
import os

DIR = os.getcwd() + '\\data'
STORAGE = {} # будет хранить данные по стране

def get_data_from_csv(path: str):
    try:
        with open(path, 'r') as file:
            file = csv.reader(file)
            for line in file:
                print(line)

            print('Файл успешно прочитан!')

        return file
    except Exception as exc:
        return [{'status': 'Error', 'message': exc}]

def upload_data_to_csv(new_path):
    pass

filename = 'economic1.csv'

if __name__ == '__main__':
    print(DIR)
    print(get_data_from_csv(os.path.join(DIR, filename)))