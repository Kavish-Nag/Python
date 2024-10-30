from datetime import datetime, timedelta

class TimeConverter:
    def seconds_to_minutes(seconds):
        return seconds / 60
    def seconds_to_hours(seconds):
        return seconds / 3600
    def seconds_to_days(seconds):
        return seconds / 86400
    def minutes_to_seconds(minutes):
        return minutes * 60
    def minutes_to_hours(minutes):
        return minutes / 60
    def minutes_to_days(minutes):
        return minutes / 1440
    def hours_to_seconds(hours):
        return hours * 3600
    def hours_to_minutes(hours):
        return hours * 60
    def hours_to_days(hours):
        return hours / 24
    def days_to_seconds(days):
        return days * 86400
    def days_to_minutes(days):
        return days * 1440
    def days_to_hours(days):
        return days * 24
      
    def to_24_hour_format(time_str):
        # Convert 12-hour time to 24-hour format
        in_time = datetime.strptime(time_str, "%I:%M %p")
        return in_time.strftime("%H:%M")
      
    def to_12_hour_format(time_str):
        # Convert 24-hour time to 12-hour format
        in_time = datetime.strptime(time_str, "%H:%M")
        return in_time.strftime("%I:%M %p")

    def add_time(time_str, hours=0, minutes=0, seconds=0):
        # Add hours, minutes, and seconds to a given time in HH:MM:SS format
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        new_time = (time_obj + delta).time()
        return new_time.strftime("%H:%M:%S")

    def subtract_time(time_str, hours=0, minutes=0, seconds=0):
        # Subtract hours, minutes, and seconds from a given time in HH:MM:SS format
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        new_time = (time_obj - delta).time()
        return new_time.strftime("%H:%M:%S")

converter = TimeConverter()

#examples
# Time unit conversions
print("150 seconds to minutes:", converter.seconds_to_minutes(150))
print("10 hours to minutes:", converter.hours_to_minutes(10))

# Time format conversions
print("12-hour to 24-hour:", converter.to_24_hour_format("02:45 PM"))
print("24-hour to 12-hour:", converter.to_12_hour_format("16:00"))

# Adding and subtracting time
print("Add 1 hour and 30 minutes:", converter.add_time("12:45:00", hours=1, minutes=30))
print("Subtract 45 minutes:", converter.subtract_time("12:45:00", minutes=45))
