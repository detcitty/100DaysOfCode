# https://www.codewars.com/kata/56bcaedfcf6b7f2125001118/train/python

def html_special_chars(data): 
    # your code here
    replace_keys = {
        '&' : '&amp;',
        '<' : '&lt;',
        '>' : '&gt;',
        '"' : '&quot;'
    }
    for word, initial in replace_keys.items():
        data = data.replace(word, initial)
    return(data)