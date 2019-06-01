# https://www.codewars.com/kata/55e2adece53b4cdcb900006c/train/python
import math

def race(v1, v2, g):
    # your code


    time = g / (v2 - v1)

    hour = math.ceil(time)

    remainder = time - math.ceil(time)

    minutes = remainder * 60

    seconds_remainder = minutes - math.ceil(minutes)

    seconds = seconds_remainder * 60

    results = [math.ceil(hour), math.ceil(minutes), math.ceil(seconds)]

    return results

print(race(80, 100, 40))
