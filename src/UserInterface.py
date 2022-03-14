def get_time_of_day():
    user_time = input("Please enter a time of day or type 'Full Day'\n")
    if user_time == 'Full Day':
        time_in_minutes = 1440
    else:
        time_in_minutes = convert_time_to_time_in_minutes(user_time)
    return time_in_minutes


def convert_time_to_time_in_minutes(user_time):
    hours_str, minutes_str = user_time.split()[0].split(sep=":")
    am_pm_flag = user_time.split()[1].lower()
    hours = int(hours_str)
    minutes = int(minutes_str)

    # Check for presence of "a.m." in user_time
    if am_pm_flag == 'a.m.':
        time_in_minutes = hours * 60 + minutes
        return time_in_minutes

    # If not a.m. then assume p.m.
    else:
        time_in_minutes = (int(hours_str) + 12) * 60 + int(minutes_str)
        return time_in_minutes