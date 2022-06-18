# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    unique_nums = set(seq)
    tracks = dict.fromkeys(unique_nums, 0)
    #tracks = {}
    #for i, e in enumerate(unique_nums):
    #    tracks[e] = 0
    
    for x in seq:
        if x in tracks.keys():
            tracks[x] += 1
    
    found_value = 0
    for indx, (key, value) in enumerate(tracks.items()):
        if value % 2 == 1:
            found_value = key
        else:
            continue 
    return found_value
