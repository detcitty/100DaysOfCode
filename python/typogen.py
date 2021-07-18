# https://www.codewars.com/kata/55953e906851cf2441000032/train/python

def scramble_words(words):
	#your code here
	words_list = words.split(r"\s+")
	new_string = ""

	for w in words_list:
		word_indices = list(range(len(w)))

		for char, i in enumerage(w):
			pass
	return(new_string)