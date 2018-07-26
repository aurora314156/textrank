
import csv
from PosTagging import posTagging

def textrankGet(n):
    # read textrank result
    with open('./textrankRes/' + n + '.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        column = [row[0] for row in reader]

    # experiment value top k keyword of 40%/50%/60%
    exp_value = [0.4, 0.5, 0.6]
    keyword = []
        
    # get textrank top k% keyword from csv
    for e in exp_value:
        ind = 0
        temp = []
        for c in column:
            if ind == (200*e):
                break
            # check word is Noun, call jieba pos tagging func
            isNoun = posTagging(c)
            if isNoun == 1:
                temp.append(c)
            ind += 1
        keyword.append(temp)
        
    return keyword