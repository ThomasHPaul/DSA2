from ChainingHashTable import ChainingHashTable
import PackageLoader
import DistanceLoader
import Truck
import SortingAlgo

PACKAGE_SRC = r"../data/prepared_package_table_v2.csv"
DISTANCE_SRC = r"../data/prepared_distance_table_v4.csv"

HOME_ADDRESS = '4001 South 700 East'


def main():
    packages = PackageLoader.load_data(PACKAGE_SRC)
    hash_table = ChainingHashTable()
    for package in packages:
        hash_table.insert(package.id, package)
    distances = DistanceLoader.load_data(DISTANCE_SRC)

    package_ids_to_deliver_truck1 = [2, 13, 14, 15, 16, 0, 19, 20, 35, 33, 17, 8, 26, 34, 7, 29]
    unsorted_packages_for_truck_1 = [hash_table.pop(id) for id in package_ids_to_deliver_truck1]

    package_ids_to_deliver_truck2 = [12, 4, 38, 37, 28, 6, 30, 39, 24, 25, 31, 1, 18, 5, 3, 36]
    unsorted_packages_for_truck_2 = [hash_table.pop(id) for id in package_ids_to_deliver_truck2]

    # final_packageIDs_to_deliver = [32,10,11,27,23,22,9,21]

    # Plan delivery route
    # Data returned -> (miles to next address, package)
    truck_1_ordered_addresses = SortingAlgo.plan_route(unsorted_packages_for_truck_1, distances)
    truck_1_last_address = truck_1_ordered_addresses[-1][1].delivery_address

    truck_2_ordered_addresses = SortingAlgo.plan_route(unsorted_packages_for_truck_2, distances)

    # Create trucks and load in packages
    truck_1 = Truck.Truck(1, 480)
    for miles, package in truck_1_ordered_addresses:
        truck_1.load_package((miles, package))

    truck_2 = Truck.Truck(2, 545)
    for miles, package in truck_2_ordered_addresses:
        truck_2.load_package((miles, package))

    # Make truck iterate through packages_on_truck and deliver in given order
    truck_1.drive_route_deliver_packages(999)
    truck_2.drive_route_deliver_packages(999)

    # truck_1.return_to_wgu(distances[truck_1_last_address][HOME_ADDRESS])
    # packages_remaining_at_wgu = [32, 10, 11, 27, 23, 22, 9, 21]
    # unsorted_packages_for_truck_1 = [hash_table.pop(id) for id in packages_remaining_at_wgu]
    # truck_1_ordered_addresses = SortingAlgo.plan_route(unsorted_packages_for_truck_1, distances)
    #
    # for miles, package in truck_1_ordered_addresses:
    #     truck_1.load_package((miles, package))

    # truck_1.drive_route_deliver_packages()

    print("Total miles driven: " + str(truck_1.get_total_miles_traveled() + truck_2.get_total_miles_traveled()))

    [print(package) for package in packages]


if __name__ == "__main__":
    main()


#
# packageIDs_to_deliver_truck1 = [12,13,14,15,16,18,19,20,38,33,4,8,26,34,7,29]
# packageIDs_to_deliver_truck2 = [2,17,35,37,28,0,30,39,24,25,31,1,32,10,27,36]


