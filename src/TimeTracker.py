class TimeTracker:
    START_TIME = 480  # 8:00 AM
    CURRENT_TIME = START_TIME

    def add_time(self, time):
        self.CURRENT_TIME += time

    def convert_to_military_time(self):
        hours = int(self.CURRENT_TIME // 60)
        minutes = str(int(self.CURRENT_TIME - (hours * 60)))
        if len(str(minutes)) == 1:
            minutes = "0" + minutes
        return f"{hours}:{minutes}"

    def __repr__(self):
        return f"Current time: {self.convert_to_military_time()}"


if __name__ == "__main__":
    timeTracker = TimeTracker()
    test_time_delta = 5.333339
    timeTracker.add_time(test_time_delta)

    print(timeTracker)
