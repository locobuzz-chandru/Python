import csv
import pandas


def write_csv():
    fields = ['Name', 'Branch', 'Year', 'CGPA']

    rows = [['Nikhil', 'COE', '2', '9.0'],
            ['Sanchit', 'COE', '2', '9.1'],
            ['Aditya', 'IT', '2', '9.3'],
            ['Sagar', 'SE', '1', '9.5'],
            ['Prateek', 'MCE', '3', '7.8'],
            ['Sahil', 'EP', '2', '9.1']]
    filename = "csv_file1.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


def read_csv():
    filename = "csv_file1.csv"
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    #     print("Total no. of rows:", csvreader.line_num)
    # print('Field names are:' + ', '.join(field for field in fields))
    # print('First 5 rows are:')
    list_ = []
    for row in rows:
        for col in row:
            list_.append(col)
    return list_


def create_dict_csv():
    with open('csv_file2.csv', 'w', newline='') as file:
        fieldnames = ['player_name', 'fide_rating']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
        writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
        writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})


def read_dict_csv():
    with open("csv_file2.csv", 'r') as file:
        csv_file = csv.DictReader(file)
        list_ = []
        for row in csv_file:
            list_.append(row)
        return list_


def read_pandas():
    df = pandas.read_csv('csv_file2.csv')
    return df


if __name__ == '__main__':
    # write_csv()
    # print(read_csv())
    # create_dict_csv()
    # print(read_dict_csv())
    print(read_pandas())
