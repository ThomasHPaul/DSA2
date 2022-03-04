class Package:
    def __init__(self, package_id, address, deadline_as_time_delta, city, zip_code, weight):
        self.id = package_id
        self.delivery_address = address
        self.deadline_as_time_delta = deadline_as_time_delta
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.status = 'at the hub'
        self.other_packages_on_truck = []

    def load_package_on_truck(self, truck_number):
        self.status = f'en route on truck {truck_number}'
        return self

    def deliver_package(self, time):
        # time should be a time_delta that is converted when displayed
        # by the interface
        self.status = f'delivered at {time}'
        return self

    def get_status(self):
        return self.status

    def __repr__(self):
        return f'Package {self.id} is {self.status}'

