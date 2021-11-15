def minutes_to_days(minutes):
    minute = 60
    hour = 24
    day_in_minutes = minute * hour

    return round(minutes / day_in_minutes, 2)


print(minutes_to_days(12347))
