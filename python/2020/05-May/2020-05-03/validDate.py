# https://www.codewars.com/kata/548db0bd1df5bbf29b0000b7/train/python
import re

pattern = "(\[\d\d-\d\d\])"
boject = re.search(pattern, "ignored [08-11] ignored") 
print(boject.groups())
if boject:
    print(boject.expand("-"))

#valid_date = 
