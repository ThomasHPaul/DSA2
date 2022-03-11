class TimeTracker:  # 8:00 AM
    def add_time(self, time):
        self.current_time = self.hypothetical_time

    def add_hypothetical_time(self, time):
        self.hypothetical_time += time

    def convert_to_military_time(self):
        hours = int(self.current_time // 60)
        minutes = str(int(self.current_time - (hours * 60)))
        if len(str(minutes)) == 1:
            minutes = "0" + minutes
        return f"{hours}:{minutes}"

    def __repr__(self):
        return f"Current time: {self.convert_to_military_time()}"

    def __init__(self, start_time_in_minutes):
        self.START_TIME = start_time_in_minutes
        self.current_time = self.START_TIME
        self.hypothetical_time = self.START_TIME


if __name__ == "__main__":
    timeTracker = TimeTracker()
    test_time_delta = 5.333339
    timeTracker.add_time(test_time_delta)

    print(timeTracker)
