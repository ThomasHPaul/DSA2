import TimeTracker


class Truck:
    SPEED = 0.299999999999  # Miles per Minute
    MAX_PACKAGES = 16  # Maximum amount of packages truck can carry at once

    def __init__(self, truck_id, start_time_in_minutes):
        self.truck_id = truck_id
        self.timeTracker = TimeTracker.TimeTracker(start_time_in_minutes)
        self.packages_on_truck = []  # Packages currently loaded onto truck
        self.total_miles_traveled = 0.0

    def __repr__(self):
        package_ids = [package.id for package in self.packages_on_truck]
        return f"{self.truck_id}"  # list total miles traveled, packages currently loaded

    def drive_route_deliver_packages(self, time_in_minutes):

        # compare hypothetical time to time_in_minutes
        for miles, package in self.packages_on_truck[:]:
            minutes_time_delta = self._calculate_time_delta_from_miles(miles)
            self.timeTracker.add_hypothetical_time(minutes_time_delta)
            if self.timeTracker.hypothetical_time < time_in_minutes:
                self._drive(miles)
                self._deliver_package(miles, package)
                self.packages_on_truck.pop(0)
            else:
                pass

        # proceed with delivery if hypothetical time < time_in_minutes

        # for miles, package in self.packages_on_truck:
        #     self._drive(miles)
        #     self._deliver_package(miles, package)
        # self.packages_on_truck = []

    def return_to_wgu(self, miles):
        self._drive(miles)

    def _deliver_package(self, miles, package):
        minutes_time_delta = self._calculate_time_delta_from_miles(miles)
        self.timeTracker.add_time(minutes_time_delta)
        package.deliver_package(self.timeTracker.convert_to_military_time())

    def _calculate_time_delta_from_miles(self, miles):
        time_delta = miles / self.SPEED
        return time_delta

    def _drive(self, miles):
        self.total_miles_traveled += miles

    def get_total_miles_traveled(self):
        return self.total_miles_traveled

    def load_package(self, package):
        if len(self.packages_on_truck) > 16:
            raise Exception("Truck can only carry 16 packages at a time")
        else:
            self.packages_on_truck.append(package)
            package[1].load_package_on_truck(self.truck_id)

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
