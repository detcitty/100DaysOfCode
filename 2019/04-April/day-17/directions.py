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
    path = arr

    i = 0
    len_path = len(path)


    while(i < len_path - 1):
        if(opposite(path[i], path[i+1])):
            del path[i]
            del path[i]
            i = 0
            len_path -= 2
        else:
            i += 1

    return path

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
