# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
import re

def domain_name(url):
	'''
	I don't know what this does. I bet it's supposed to clear a url.
	'''
	beginning_regex = r"^(http[s]?)?(\:\/+)?(w{3}\.?)?"
	mod_string = re.sub(beginning_regex, '', url, flags=re.I)
	next_part = r"^[^\.]*"
	begin_name = re.match(next_part, mod_string, flags=re.I)
	return(begin_name[0])


test1 = domain_name("http://www.google.com")
test2 = domain_name("http://google.co.jp")
test3 = domain_name("www.xakep.ru")
test4 = domain_name("https://youtube.com")

print(test1)
print(test4)