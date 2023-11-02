from glob import glob

from flatten_json import flatten
import json
import csv
import os


def main():
    for json_file_name in glob('data/**/*.json', recursive=True):
        with open(json_file_name) as json_file:
            json_data = flatten(json.load(json_file), '_')
            data_file = open(os.path.splitext(json_file_name)[0] + '.csv', 'w', newline='')
            csv_writer = csv.writer(data_file)
            csv_writer.writerow([data for data in json_data])
            csv_writer.writerow([json_data[data] for data in json_data])
            data_file.close()
    pass


if __name__ == "__main__":
    main()
