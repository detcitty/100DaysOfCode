# https://www.codewars.com/kata/56bcaedfcf6b7f2125001118/train/python

def html_special_chars(data): 
    # your code here
	keys = {
        '<' : '&lt;',
        '>' : '&gt;',
        '"' : '&quot;',
        '&' : '&amp;'
    }