#https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def order(sentence):
    # code here
    data = {}
    if(len(sentence) == 0):
        return("")

    separate = sentence.split()
    for i in range(len(separate)):
        x = [int(s) for s in separate[i] if s.isdigit()]
        key = x[0]
        data.update({key: separate[i]})
        print(x)

    final_str = ""
    for i in range(len(separate)):
        final_str += data[i] + " "
    print(data)

    return(final_str)

order("is2 Thi1s T4est 3a")
