import TimeTracker


class Truck:
    SPEED = 0.299999999999  # Miles per Minute
    MAX_PACKAGES = 16  # Maximum amount of packages truck can carry at once
    HOME_ADDRESS = '4001 South 700 East (84107)'

    packages_on_truck = []  # Packages currently loaded onto truck
    total_miles_traveled = 0.0

    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.timeTracker = TimeTracker.TimeTracker()

    def __repr__(self):
        pass  # list total miles traveled, packages currently loaded

    def deliver_packages(self, current_address, miles):
        for package in self.packages_on_truck:
            if package.delivery_address == current_address:
                minutes_time_delta = self._calculate_time_delta_from_miles(miles)
                self.timeTracker.add_time(minutes_time_delta)
                package.deliver_package(self.timeTracker.convert_to_military_time())
                self.packages_on_truck.remove(package)

    def _calculate_time_delta_from_miles(self, miles):
        time_delta = miles / self.SPEED
        return time_delta

    def drive(self, miles):
        self.total_miles_traveled += miles

    def get_total_miles_traveled(self):
        return self.total_miles_traveled

    def load_package(self, package):
        self.packages_on_truck.append(package)

    def get_packages_on_truck(self):
        return self.packages_on_truck

    def get_all_other_packages(self, package):
        all_other_packages = [x for x in self.packages_on_truck if x != package]
        return all_other_packages

    def packages_still_on_truck(self):
        if len(self.packages_on_truck) == 0:
            return False
        else:
            return True
