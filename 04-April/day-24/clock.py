def what_is_the_time(time_in_mirror):
    # Your code here
    time = time_in_mirror.split(":")
    print(time)
    hour = int(time[0])
    minute = int(time[1])
    print(hour)
    print(minute)
    hour_mirror = 12 - (hour % 12) - 1
    minute_mirror = 60 - (minute % 60)
    print(hour_mirror)
    print(minute_mirror)

what_is_the_time("06:35")
what_is_the_time("11:59")
what_is_the_time("04:00")
