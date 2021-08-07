import re

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    found_index = []
    found = False
    for i, doc in enumerate(doc_list):
        lower_doc_orig = doc.lower()
        lower_doc_clean = re.sub(r'[^\w]', ' ', lower_doc_orig).split()
        for word in lower_doc_clean:
            if keyword == word:
                print("{} == {}".format(keyword, word))
                found = True
                found_index.append(i)
                break
            else:
                continue
    value = found_index if found else [] 
    return(value)
                    
        

# Check your answer
q2.check()