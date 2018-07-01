import csv
from hanziconv import HanziConv

def textrankRes(name,trRes):
    with open(name + '.csv', 'w', newline='', encoding = 'utf-16') as res:
        writer = csv.writer(res)
        for k, v in trRes:
            writer.writerow([str(HanziConv.toTraditional(k)), str(v)])
    res.close()
