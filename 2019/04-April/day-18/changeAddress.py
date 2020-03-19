# https://www.codewars.com/kata/52ea928a1ef5cfec800003ee/train/python

def binary(bit):
    start = bit
    rounds = []
    remainder = []
    while(start > 1):

        left_over = start % 2
        start = int(round(start / 2))


        rounds.append(start)
        remainder.append(left_over)
    return(rounds, remainder)


def ip_to_int32(ip):
  # your code here

  separated = ip.split(".")

print(binary(32))
