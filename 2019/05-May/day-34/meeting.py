# https://www.codewars.com/kata/59df2f8f08c6cec835000012/train/python

def meeting(s):
    # your code
    list_string = s.split(";")
    corrected_names = []
    final_string = ""
    for name in list_string:
        sep_name = name.split(":")
        #print(sep_name)

        combinded = "(" + sep_name[1].upper()+ ", " + sep_name[0].upper() + ")"
        #print(combinded)
        corrected_names.append(combinded)
        corrected_names.sort()

    for i in corrected_names:
        final_string += i

    #corrected_names.sort()
    return final_string


meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn")
