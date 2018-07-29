import csv
import json
import os
from TextRankResGet import textrankGet
from hanziconv import HanziConv

def textrankJob(n):
    # get keyword
    keyword = textrankGet(n)
    # read testdata line by line
    for i in range(1,8):
        with open('./finalResult/'+ n +'dataset' + str(i) +'.csv', 'w', newline='', encoding = 'utf-8') as res:
            writer = csv.writer(res)
            with open('./testData/dataset' + str(i)+ '.txt', 'r', newline='', encoding='utf-8') as txtfile:
                tr = txtfile.readlines()
                flag = True
                for t in tr:
                    if flag is True:
                        article = t
                    else:
                        # store keyword match on article content
                        keywordMatch = []
                        content = t
                        # start match keyword and content
                        for index in keyword:
                            temp = []
                            for k in index:
                                if n == 'tfidf':
                                    k = HanziConv.toTraditional(k)
                                if k in content:
                                    temp.append(k)
                            keywordMatch.append(temp)
                        # write match result to csv
                        writer.writerow([article.strip()])
                        writer.writerow([content.strip()])
                        if n == 'tfidf':
                            tempkeyword = []
                            string = "Result:"
                            tempkeyword.append(string)
                            for k in keywordMatch[0]:
                                tempkeyword.append(k)
                            writer.writerow(tempkeyword)
                            writer.writerow("\n")
                        else:
                            exp_value = [0.4, 0.5, 0.6]
                            for j in range(3):
                                tempkeyword = []
                                tempkeyword.append(exp_value[j])
                                for k in keywordMatch[j]:
                                    tempkeyword.append(k)
                                writer.writerow(tempkeyword)
                            writer.writerow("\n")

                    flag = not flag

    print("------------------------------------------")