import csv


def load_data(src):
    location_dict = {}

    with open(src) as distance_csv:
        csv_reader = csv.reader(distance_csv, delimiter=',')

        # Skip column names contained in the first line
        next(distance_csv)
        for row in csv_reader:
            src_address = row[0]
            location_dict[src_address] = {}

        distance_csv.seek(0)
        next(distance_csv)
        for row in csv_reader:
            src_address = row[0]
            dst_address = row[1]
            miles = float(row[2])
            location_dict[src_address][dst_address] = miles

    return location_dict


if __name__ == "__main__":
    src = r'../data/prepared_distance_table_v4.csv'
    location_dict = load_data(src)
    print(len(location_dict))
    print(location_dict['4001 South 700 East']['1330 2100 S'])
