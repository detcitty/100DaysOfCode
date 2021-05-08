# https://www.codewars.com/kata/57ebdf1c2d45a0ecd7002cd5/train/python

def inside_out(st):

    
    
    end = ''
    
    for e in st.split(" "):
        values = list(e)
        while len(values) != 0:
            end += values.pop(-1)
        end += " "

    return(end.strip())

test = "man i need a taxi up to ubud"
print(inside_out(test))
