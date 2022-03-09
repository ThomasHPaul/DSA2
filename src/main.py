from ChainingHashTable import ChainingHashTable
import PackageLoader
import DistanceLoader
import Truck
import SortingAlgo

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
    unsorted_packages_for_truck_1 = [hash_table.search(id) for id in package_ids_to_deliver_truck1]

    # Plan delivery route
    truck_1_ordered_addresses = SortingAlgo.plan_route(unsorted_packages_for_truck_1, distances)

    # Create truck and load in packages
    truck_1 = Truck.Truck(1)
    for miles, package in truck_1_ordered_addresses:
        truck_1.load_package(package)

    # Load packages into package_list
    for id in package_ids_to_deliver_truck1:
        package = hash_table.search(id)
        truck_1.load_package(package)

    # truck_1_ordered_addresses = SortingAlgo.plan_route(truck_1, distances)

    # # Print for troubleshooting
    # print("ordered addresses: ")
    # for miles, package in ordered_addresses:
    #     if len(str(miles)) < 3:
    #         print(miles, "\t\t", package.id, "\t", package.delivery_address, "\t")
    #     else:
#         print(miles, "\t", package.id, "\t" if len(str(package.id)) > 1 else "\t\t", package.delivery_address, "\t")

    # Make truck iterate through packages_on_truck and deliver in given order

    for miles, package in truck_1_ordered_addresses:
        print("id:", package.id, "miles:", miles, "\t\t", "Package", package.status)




if __name__ == "__main__":
    main()


#
# packageIDs_to_deliver_truck1 = [12,13,14,15,16,18,19,20,38,33,4,8,26,34,7,29]
# packageIDs_to_deliver_truck2 = [2,17,35,37,28,0,30,39,24,25,31,1,32,10,27,36]
# final_packageIDs_to_deliver = [6,5,11,3,23,22,9,21]

