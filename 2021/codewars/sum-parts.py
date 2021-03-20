# https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python

def parts_sums(ls):
    # your code
    
    lists = [i for i in range(len(ls))]
    print(lists)
    calc = lambda x, y: sum(x[y:])
    results = [calc(ls,p) for p in lists]
    #print(lists)
    return(results)

syn = parts_sums([0, 1, 3, 6, 10])
print(syn)