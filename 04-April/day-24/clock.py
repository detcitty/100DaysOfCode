def what_is_the_time(time_in_mirror):
    # Your code here
    time = time_in_mirror.split(":")
    print(time)
    hour = int(time[0])
    minute = int(time[1])
    print(hour)
    print(minute)

what_is_the_time("06:35")
