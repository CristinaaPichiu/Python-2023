import csv


def read_csv(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(row)
    return data
