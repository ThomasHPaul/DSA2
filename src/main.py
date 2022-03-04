from ChainingHashTable import ChainingHashTable
import PackageLoader
import DistanceLoader
import Truck

PACKAGE_SRC = r"../data/prepared_package_table_v2.csv"
DISTANCE_SRC = r"../data/prepared_distance_table_v4.csv"

TEST_TIME = 0

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
    start_address = "4001 South 700 East"
    dst_list = []

    # Sorting algo
    while truck_1.packages_still_on_truck():

        # Load package distances & select the first closest destination
        for package in truck_1.get_packages_on_truck():
            dst_list.append((distances[start_address][package.delivery_address], package))

        dst_list.sort(key=lambda x: x[0])
        ordered_addresses.append(dst_list[0])
        truck_1.deliver_packages(dst_list[0][1].delivery_address, TEST_TIME)

        for other_package in truck_1.get_all_other_packages(ordered_addresses[0][1]):
            if start_address == other_package.delivery_address:
                ordered_addresses.append((0, other_package))
                truck_1.deliver_packages(other_package.delivery_address, TEST_TIME)

    # Print for troubleshooting
    print("ordered addresses: ")
    for miles, package in ordered_addresses:
        if len(str(miles)) < 3:
            print(miles, "\t\t", package.id, "\t", package.delivery_address, "\t")
        else:
            print(miles, "\t", package.id, "\t", package.delivery_address, "\t")


if __name__ == "__main__":
    main()


#
# packageIDs_to_deliver_truck1 = [12,13,14,15,16,18,19,20,38,33,4,8,26,34,7,29]
# packageIDs_to_deliver_truck2 = [2,17,35,37,28,0,30,39,24,25,31,1,32,10,27,36]
# final_packageIDs_to_deliver = [6,5,11,3,23,22,9,21]

