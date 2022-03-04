import csv
from Package import Package


def load_data(src):
    package_list = []

    with open(src) as package_csv:
        csv_reader = csv.reader(package_csv, delimiter=',')

        # Skip column names contained in the first line
        headers = next(csv_reader)

        for row in csv_reader:
            package_id = int(row[0])
            address = row[1]
            deadline_as_time_delta = (row[2])
            city = row[3]
            zip_code = row[4]
            weight = row[5]

            package = Package(package_id, address, deadline_as_time_delta, city, zip_code, weight)

            package_list.append(package)

    return package_list


if __name__ == "__main__":
    src = SOURCE = r'../data/prepared_package_table_v2.csv'
    package_list = load_data(src)
    print(package_list)
