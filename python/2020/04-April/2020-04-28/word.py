# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python


def abbrevName(name):
    names = name.split(" ")
    first = names[0]
    last = names[1]

    f = first[0]
    l = last[0]

    return(f"{f.upper()}.{l.upper()}")

print(abbrevName("Devin Etcitty"))