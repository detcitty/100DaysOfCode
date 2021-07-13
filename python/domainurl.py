# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
import re

def domain_name(url):
	beginning_regex = r'(http[s]?)?(\:\/+)?(w{3}\.?)'
	mod_string = re.sub(beginning_regex, '', url, re.IGNORECASE)
	return(mod_string)


test1 = domain_name("http://google.com")
test2 = domain_name("http://google.co.jp")
test3 = domain_name("www.xakep.ru")
test4 = domain_name("https://youtube.com")

print(test1)
print(test4)