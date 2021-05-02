# https://www.kaggle.com/detcitty/exercise-strings-and-dictionaries/edit

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
    found = 0
    for i, doc in enumerate(doc_list):
        lower_doc = doc.lower().strip('.').split()
        for word in lower_doc:
            if keyword in word:
                found = i
                print("here")
                print(keyword)
                break
            else:
                continue
    return([found])

test_ = """I like the New Yorker magazine.
I have been to New York City. 
New York state is also the Empire State.
"""

example_ = word_search(test, 'New York')
