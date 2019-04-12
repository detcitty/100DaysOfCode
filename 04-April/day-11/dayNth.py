# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

def delete_nth(order,max_e):
    # code here

    #create dictionary to count instances of number
    unique_numbers = set(order)

    bag = {}

    for i in range(len(unique_numbers)):
        bag.update({unique_numbers[i], 0})

    for i in range(len(order)):
        print(bag[order[i]])




delete_nth([20,37,20,21], 1)
delete_nth([1,1,3,3,7,2,2,2,2], 3)
