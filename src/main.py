from ChainingHashTable import ChainingHashTable
import PackageLoader
import DistanceLoader
import Truck

PACKAGE_SRC = r"../data/prepared_package_table_v2.csv"
DISTANCE_SRC = r"../data/prepared_distance_table_v4.csv"

TEST_TIME = 0


class Time:
    DAY_START = 480  # 8:00 AM
    MINUTES_PER_HOUR = 60
    CURRENT_TIME = DAY_START

    def calculate_time(self, time_delta):
        pass
    # function should take time and return military time formatted hours



def main():
    packages = PackageLoader.load_data(PACKAGE_SRC)
    hash_table = ChainingHashTable()
    for package in packages:
        hash_table.insert(package.id, package)

    distances = DistanceLoader.load_data(DISTANCE_SRC)
    package_ids_to_deliver_truck1 = [12, 13, 14, 15, 16, 18, 19, 20, 38, 33, 4, 8, 26, 34, 7, 29]
    truck_1 = Truck.Truck(1)

    # Load packages into package_list
    for id in package_ids_to_deliver_truck1:
        package = hash_table.search(id)
        truck_1.load_package(package)

    ordered_addresses = []
    current_address = "4001 South 700 East"

    # Sorting algo
    while truck_1.packages_still_on_truck():
        dst_list = []

        # Load package distances & select the first closest destination
        for package in truck_1.get_packages_on_truck():
            dst_list.append((distances[current_address][package.delivery_address], package))

        dst_list.sort(key=lambda x: x[0])
        ordered_addresses.append(dst_list[0])
        i = 1
        miles = dst_list[0][0]
        current_package = dst_list[0][1]
        current_address = current_package.delivery_address
        truck_1.deliver_packages(current_address, miles)
        for miles, package in dst_list:
            if package.delivery_address == current_address and package != current_package:
                ordered_addresses.append((0, package))
                truck_1.deliver_packages(package.delivery_address, 0)

    # Print for troubleshooting
    print("ordered addresses: ")
    for miles, package in ordered_addresses:
        if len(str(miles)) < 3:
            print(miles, "\t\t", package.id, "\t", package.delivery_address, "\t")
        else:
            print(miles, "\t", package.id, "\t" if len(str(package.id)) > 1 else "\t\t", package.delivery_address, "\t")

    for miles, package in ordered_addresses:
        print("id:", package.id, "miles:", miles, "\t\t", "Package", package.status)


if __name__ == "__main__":
    main()


#
# packageIDs_to_deliver_truck1 = [12,13,14,15,16,18,19,20,38,33,4,8,26,34,7,29]
# packageIDs_to_deliver_truck2 = [2,17,35,37,28,0,30,39,24,25,31,1,32,10,27,36]
# final_packageIDs_to_deliver = [6,5,11,3,23,22,9,21]

