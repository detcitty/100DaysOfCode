# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python
from functools import reduce

def DNA_strand(dna):
    # code here
    dna_translate = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    str_replaced = reduce(lambda x, y: x.replace(*y), [list(dna), *list(dna_translate.items())])
