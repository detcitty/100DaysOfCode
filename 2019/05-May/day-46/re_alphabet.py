
# https://www.codewars.com/kata/5938f5b606c3033f4700015a/train/python
import re

def alphabet_war(fight):
    #your code here

    score = re.compile('[^\w](?!\*)(?<!\*)')
    results = re.findall(score, fight)
    print(results)


alphabet_war("z*dq*mw*pb*s")
alphabet_war("z*z*z*zs")