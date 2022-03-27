# https://www.codewars.com/kata/52ebe4608567ade7d700044a/train/python

def encode(cards):
    values = list(map(lambda x: list(x), cards))
    final_list = []
    for num, card in values:

        dict_1 = {'A': 0, 'T': 9, 'J': 10, 'Q': 11, 'K': 12}
        card_dict = {'c': 1, 'd': 2, 'h': 3, 's': 4}
        values = 0
        if num in dict_1.keys():
            values = dict_1[num]
        else:
            values = num
        
        card_value = card_dict[card]
        combinded_card_num = values * card_value
        final_list.append(combinded_card_num)


    return

def decode(cards):
    return