
import csv
from PosTagging import posTagging

def textrankGet(n):
    # read csv word result
    with open('./textrankRes/' + n + '.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        column = [row[0] for row in reader]
    # read csv value result
    with open('./textrankRes/' + n + '.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        value = [row[1] for row in reader]

    # experiment value top k keyword of 40%/50%/60%
    exp_value = [0.4, 0.5, 0.6]
    keyword = []
    
    # cal tfidf result
    if n == 'tfidf':
        temp = []
        for i in range(len(column)):
            # tfidf result break, by 0.385 threshold
            if float(value[i]) < 0.385:
                break
            # check word is Noun, call jieba pos tagging func
            isNoun = posTagging(column[i], n)
            if isNoun == 1:
                temp.append(column[i])
        keyword.append(temp)

    # get textrank top k% keyword from csv
    else:
        for e in exp_value:
            ind = 0
            temp = []
            for c in column:
                if ind == (200*e):
                    break
                # check word is Noun, call jieba pos tagging func
                isNoun = posTagging(c, n)
                if isNoun == 1:
                    temp.append(c)
                ind += 1
            keyword.append(temp)
    print("HI")
    return keyword