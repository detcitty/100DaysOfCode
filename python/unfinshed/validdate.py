# https://www.codewars.com/kata/548db0bd1df5bbf29b0000b7/train/python
# Merged files
# ./python/2020/05-May/2020-05-03/validDate.py
'''
What does this return?
A value or do I just need to come up with the regex?
'''
import re

valid_date = r'[01][01-31]|[02][01-28]|[03][01-30]'

pattern = "(\[\d\d-\d\d\])"
boject = re.search(pattern, "ignored [08-11] ignored") 
print(boject.groups())
if boject:ma
    print(boject.expand("-"))

#valid_date = 
