# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

def delete_nth(order,max_e):
    # code here

    #create dictionary to count instances of number
    bag = {}
    new_list = []
    
    for i in range(len(order)):
        keys = bag.keys()
        new_list.append(order[i])
        if(order[i] not in keys):
            bag.update({order[i], 0})
        elif(bag[order[i]] < max_e):
            number = bag[order[i]]
            bag.update({order[i], number+1})
        else:
            del new_list[i]

    print(bag[order[i]])
    return(new_list)



delete_nth([20,37,20,21], 1)
delete_nth([1,1,3,3,7,2,2,2,2], 3)
