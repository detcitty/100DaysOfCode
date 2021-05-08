import re
regex_exp = "(\.)(\d*$)"
value = "2"
test = re.search(regex_exp, value)

print(test.groups())