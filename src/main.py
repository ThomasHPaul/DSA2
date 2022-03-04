from ChainingHashTable import ChainingHashTable
import PackageLoader
import DistanceLoader
import Truck

PACKAGE_SRC = r"../data/prepared_package_table_v2.csv"
DISTANCE_SRC = r"../data/prepared_distance_table_v4.csv"


def main():
    packages = PackageLoader.load_data(PACKAGE_SRC)
    hash_table = ChainingHashTable()
    for package in packages:
        hash_table.insert(package.id, package)

    distances = DistanceLoader.load_data(DISTANCE_SRC)
    package_ids_to_deliver_truck1 = [12, 13, 14, 15, 16, 18, 19, 20, 38, 33, 4, 8, 26, 34, 7, 29]
    package_list = []
    truck_1 = Truck.Truck(1)

    # Load packages into package_list
    for id in package_ids_to_deliver_truck1:
        package = hash_table.search(id)
        # package_list.append(package)
        truck_1.load_package(package)

    # For each package, load other packages into other_packages list
    # for i, package in enumerate(package_list):
    #     for other_package in package_list:
    #         if package_list[i] == other_package:
    #             pass
    #         else:
    #             package.other_packages_on_truck.append(other_package)

    ordered_addresses = []
    start_address = "4001 South 700 East"

    # Sorting algo
    # for i, package in enumerate(package_list):
    for i, package in enumerate(truck_1.get_packages_on_truck()):
        dst_list = []

        # If first delivery then start = WGU's address: 4001 South 700 East
        # Else use package's delivery_address
        if i != 0:
            start_address = package.delivery_address

        # If any other packages have same delivery_address then add as (0 miles, package with same delivery_address)
        # Else add (distance, package)
        # for other_package in package.other_packages_on_truck:
        #     if start_address == other_package.delivery_address:
        #         dst_list.append((0, other_package))
        #     else:
        #         dst_list.append((distances[start_address][other_package.delivery_address], other_package))
        for other_package in truck_1.get_all_other_packages(package):
            if start_address == other_package.delivery_address:
                dst_list.append((0, other_package))
                ### When this for loop assigns 0 and the list is sorted, other packages besides the one chosen to
                ### deliver are moved ahead and the original package for delivery is passed by
                ### ANOTHER CONCERN is that the initial list sorting happens AFTER 0 has been assigned. REALLY first
                ### an overall sort should happen THEN AFTER the next destination is decided, other packages with the
                ### same address can have their distance traveled, set to 0!!!
            else:
                dst_list.append((distances[start_address][other_package.delivery_address], other_package))

        # Sort dst_list to grab the shortest distance
        dst_list.sort(key=lambda x: x[0])

        # Add shortest distance to ordered_addresses
        ordered_addresses.append(dst_list[0])
        truck_1.deliver_packages(dst_list[0][1].delivery_address, 0)
        # Remove sorted package from all other packages
        # for package in package_list:
        #     if dst_list[0][1] in package.other_packages_on_truck:
        #         package.other_packages_on_truck.remove(dst_list[0][1])
        #     else:
        #         pass

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

