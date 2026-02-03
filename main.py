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


def upload_data_to_csv(new_path: str, data):
    with open(new_path, 'w', newline='') as output_file:
        output_file = csv.writer(output_file)
        output_file.writerow(['country', 'gpd'])

        for line in data:
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




if __name__ == '__main__':
    # python main.py --files economic1.csv --report ava
    parser = argparse.ArgumentParser(description='-_-')
    parser.add_argument('-f', '--files', nargs='+', type=str, default=['economic1.csv', 'economic2.csv'],
                        help='Entering file names for calculation')
    parser.add_argument('-r', '--report', type=str, default='average-gdp', help='Entering file name of output file')
    args = parser.parse_args()
    try:
        filename = args.files
        temp = filename[:]
        total = []
        for file in filename:
            for address, dirs, files in os.walk(DIR):
                if file in files:
                    temp.remove(file)
        for file in temp:
            filename.remove(file)
    except Exception as exc:
        print(f'Ошибка {exc}, попробуйте еще раз')

    output_filename = args.report + '.csv'

    for file in filename:
        file = get_data_from_csv(os.path.join(DIR, file))
        calculating_average_gdp(file)

    for country in STORAGE:
        STORAGE[country] = round(STORAGE[country][0] / STORAGE[country][1], 2)

    new_storage = sorted(STORAGE.items(), key=lambda x: x[1], reverse=True)
    upload_data_to_csv(output_filename, new_storage)
    output_tab = []
    for i, el in enumerate(new_storage):
        output_tab.append((i + 1, el[0], el[1]))
    print(tabulate.tabulate(output_tab, headers=['', 'country', 'gdp'], tablefmt='grid'))
