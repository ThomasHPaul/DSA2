def plan_route(unsorted_packages, distances):
    ordered_addresses = []
    current_address = "4001 South 700 East"

    # Greedy algorithm (always searching for next closest destination)
    while len(unsorted_packages) > 0:
        dst_list = []

        # Load package distances & select the first closest destination
        for package in unsorted_packages:
            dst_list.append((distances[current_address][package.delivery_address], package))
        dst_list.sort(key=lambda x: x[0])
        ordered_addresses.append(dst_list[0])

        current_package = dst_list[0][1]
        current_address = current_package.delivery_address
        unsorted_packages.remove(current_package)

        # Add any packages with same delivery address to ordered_addresses with 0 miles
        for miles, package in dst_list:
            if package.delivery_address == current_address and package != current_package:
                ordered_addresses.append((0, package))
                unsorted_packages.remove(package)

    return ordered_addresses
