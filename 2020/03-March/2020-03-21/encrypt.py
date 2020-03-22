def encrypt_this(text):

    words = text.split(" ")


    encrypt = ""

    if (text != ""):
        for w in words:

            first = w[:1]
            #print(first)
            last = w[-1:]
            #print(last)
            second = w[1:2]


            new_word = str(ord(first)) + last + w[2:len(w)-1] + second

            encrypt += new_word + " "
    return(encrypt.strip())

print(encrypt_this("A wise old owl lived in an oak"))
