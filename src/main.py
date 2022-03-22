# Thomas Paul 000917547

from ChainingHashTable import ChainingHashTable
import PackageLoader
import DistanceLoader
import Truck
import SortingAlgo
import UserInterface

PACKAGE_SRC = r"../data/prepared_package_table_v2.csv"
DISTANCE_SRC = r"../data/prepared_distance_table_v4.csv"

HOME_ADDRESS = '4001 South 700 East'


def main():
    # Overall big-O: n^2

    # Load in prepared csv data
    # big-O Complexity: n
    packages = PackageLoader.load_data(PACKAGE_SRC)
    hash_table = ChainingHashTable()
    for package in packages:
        hash_table.insert(package.id, package)
    distances = DistanceLoader.load_data(DISTANCE_SRC)

    # Packages hand sorted prior to running program
    # big-O Complexity: n
    package_ids_to_deliver_truck1 = [2, 13, 14, 15, 16, 0, 19, 20, 35, 33, 17, 8, 26, 34, 7, 29]
    unsorted_packages_for_truck_1 = [hash_table.pop(id) for id in package_ids_to_deliver_truck1]

    package_ids_to_deliver_truck2 = [12, 4, 38, 37, 28, 6, 30, 39, 24, 25, 31, 1, 18, 5, 3, 36]
    unsorted_packages_for_truck_2 = [hash_table.pop(id) for id in package_ids_to_deliver_truck2]

    # Plan delivery route
    # Data returned -> (miles to next address, package)
    # big-O Complexity: 2n^2
    truck_1_ordered_addresses = SortingAlgo.plan_route(unsorted_packages_for_truck_1, distances)
    truck_1_last_address = truck_1_ordered_addresses[-1][1].delivery_address

    truck_2_ordered_addresses = SortingAlgo.plan_route(unsorted_packages_for_truck_2, distances)
    truck_2_last_address = truck_2_ordered_addresses[-1][1].delivery_address

    # Create trucks and load in packages
    # big-O Complexity: 2n
    truck_1 = Truck.Truck(1, 480)
    for miles, package in truck_1_ordered_addresses:
        truck_1.load_package((miles, package))

    truck_2 = Truck.Truck(2, 545)
    for miles, package in truck_2_ordered_addresses:
        truck_2.load_package((miles, package))

    # Get time snapshot from user to check partial day's progress (or run Full Day if requested)
    # big-O Complexity: 1
    time_in_minutes = UserInterface.get_time_of_day()

    # Make truck iterate through packages_on_truck and deliver in given order
    # big-O Complexity: 2n
    truck_1.drive_route_deliver_packages(time_in_minutes)
    truck_2.drive_route_deliver_packages(time_in_minutes)

    # Truck 1 returns to get remaining packages
    # big-O Complexity: n^2 + n
    if truck_1.is_empty():
        truck_1.return_to_wgu(distances[truck_1_last_address][HOME_ADDRESS])
        packages_remaining_at_wgu = [32, 10, 11, 27, 23, 22, 9, 21]
        unsorted_packages_for_truck_1 = [hash_table.pop(id) for id in packages_remaining_at_wgu]
        truck_1_ordered_addresses = SortingAlgo.plan_route(unsorted_packages_for_truck_1, distances)
        truck_1_last_address = truck_1_ordered_addresses[-1][1].delivery_address

        for miles, package in truck_1_ordered_addresses:
            truck_1.load_package((miles, package))

        truck_1.drive_route_deliver_packages(time_in_minutes)

    # Trucks return so drivers not left in field
    # big-O Complexity: 1
    if truck_2.is_empty():
        truck_2.return_to_wgu(distances[truck_2_last_address][HOME_ADDRESS])
    if truck_1.is_empty():
        truck_1.return_to_wgu(distances[truck_1_last_address][HOME_ADDRESS])

    # Print summary of the day's progress
    # big-O Complexity: n
    print("Total miles driven: " + str(round(truck_1.get_total_miles_traveled() + truck_2.get_total_miles_traveled())))
    [print(package) for package in packages]


if __name__ == "__main__":
    main()
