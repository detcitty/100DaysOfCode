# https://www.codewars.com/kata/515e188a311df01cba000003/solutions/python

def get_planet_name(id):
    switcher = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus"  ,
        8: "Neptune",
    }
    return switcher.get(id, "nothing")

print(get_planet_name(3))