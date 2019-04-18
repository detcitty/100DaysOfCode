# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

def opposite(arr, second):
    if(arr == "NORTH" and second == "SOUTH"):
        return True
    elif(arr == "SOUTH" and second == "NORTH"):
        return True
    elif(arr == "WEST" and second == "EAST"):
        return True
    elif(arr == "EAST" and second == "WEST"):
        return True
    else:
        return False


def dirReduc(arr):
    path = []
    for i in range(len(arr)):
        if(i == len(arr) - 1):
            break
        else:
            if (opposite(arr[i]), arr[i+1]):
                continue
            else:
                path.append(append[i])
    return path

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
