class RaceAverage:

    def __init__(self, times):
        self.times = times

    def avgMinutes(self):
        total = 0.0

        # Iterate over each string in times array to get race length.
        for time in self.times:
            line = time.split()

            # Convert hours to military time.
            if line[1] == "AM," and line[0][:2] == "12":
                hour = int(line[0][:2]) - 12
            elif line[1] == "AM," or line[0][:2] == "12":
                hour = int(line[0][:2])
            else:
                hour = int(line[0][:2]) + 12

            # Set other variables for readability.
            minute = int(line[0][3:])
            day = int(line[3])
            MIN_PER_DAY = 24 * 60
            MIN_PER_HOUR = 60

            # Calculate length of race from 8:00 AM on Day 1.
            if hour >= 8:
                race_length = (day - 1) * MIN_PER_DAY + (hour - 8) * \
                    MIN_PER_HOUR + minute
            else:
                race_length = (day - 1) * MIN_PER_DAY - (8 - hour - 1) * \
                    MIN_PER_HOUR - (60 - minute)

            total += race_length

        return int(round(total / len(self.times)))

if __name__ == '__main__':

    times = ["02:00 PM, DAY 19","02:00 PM, DAY 20","01:58 PM, DAY 20"]
    ra = RaceAverage(times)
    print ra.avgMinutes()