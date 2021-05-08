# https://www.codewars.com/kata/55f3da49e83ca1ddae0000ad/train/python
import math

def tankvol(h, d, vt):
    # your code
    distance = abs(h - d)
    r =  d /2

    length = vt / (math.pi * r**2)

    theta = math.acos(float(distance) / float(r))
    print(theta)

    lateral_area = float(theta) / 2.0 * (r**2) - (r - h) * math.sqrt(h * (2-h))

    volumn = lateral_area * length
    return volumn

tankvol(2, 7, 3848)