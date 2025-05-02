class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        # Handle overflow from seconds to minutes and from minutes to hours
        self.minutes += self.seconds // 60
        self.seconds %= 60

        self.hours += self.minutes // 60
        self.minutes %= 60

    def display(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def add(self, other):
        return Time(
            self.hours + other.hours,
            self.minutes + other.minutes,
            self.seconds + other.seconds
        )

    def subtract(self, other):
        # Convert both times to seconds and subtract
        total1 = self.to_seconds()
        total2 = other.to_seconds()
        diff = abs(total1 - total2)

        return Time.from_seconds(diff)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def to_minutes(self):
        return self.hours * 60 + self.minutes + self.seconds / 60

    @staticmethod
    def from_seconds(total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return Time(int(hours), int(minutes), int(seconds))


# Example usage
t1 = Time(2, 45, 50)
t2 = Time(1, 20, 30)

print("Time 1:", end=" ")
t1.display()

print("Time 2:", end=" ")
t2.display()

print("\nAddition:", end=" ")
t3 = t1.add(t2)
t3.display()

print("Subtraction:", end=" ")
t4 = t1.subtract(t2)
t4.display()

print(f"\nTime 1 in minutes: {t1.to_minutes():.2f}")
print(f"Time 1 in seconds: {t1.to_seconds()} sec")
