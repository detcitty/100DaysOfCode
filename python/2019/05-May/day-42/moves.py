# https://www.codewars.com/kata/56dbeec613c2f63be4000be6/train/python

def str_matrix(strng):
    values = strng.split("\n")
    final_matrix = []
    #print(values)
    size = len(values)
    for i in range(size):
        middle = []
        letter = values[i]
        for j in range(size):
            middle.append(letter[j])
        final_matrix.append(middle)

    return(final_matrix)

def rot_90_clock(strng):
    # your code
    pass

def diag_1_sym(strng):
    # your code
    pass

def selfie_and_diag1(strng):
    # your code
    pass
def oper(fct, s):
    # your code
    pass

test = "rgavce\nvGcEKl\ndChZVW\nxNWgXR\niJBYDO\nSdmEKb"

str_matrix(test)
