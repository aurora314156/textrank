import csv
import json
import os

# ===== main func entry point =====
def main():

    sTime = time.time()
    # scrawler url setting
    url = "http://140.124.183.5:8983/solr/EBCStation/select?indent=on&q=*:*&rows=500&wt=json"
    request = requests.get(url).json()

    # writing to csv set up
    f = open('textRankJob.csv', 'w', newline='')
    write = csv.writer(f)
    csvtable= []

    # experiment value
    value = [0.33,0.35,0.385,0.4,0.45,0.5,0.55]
    temp = []

    # iterator all content
    for i in range(150):
        # store csv title
        content = request['response']['docs'][j]['content']
        content = HanziConv.toSimplified(content)
        temp.append('Article :'+str(j))
        write.writerow(temp)
        temp.clear()
        csvtable.append(content)
        write.writerow(csvtable)
        csvtable.clear()
        # iterator all experiment value
        for i in value:
            temp.append(i)
            # iterator all tf_idf
            for r in range(len(result)):
                # if tf_idf value bigger than experiment value
                if result[r][1] > i:
                    # then check keyword exist in content or not
                    if result[r][0] in content:
                        temp.append(HanziConv.toTraditional(result[r][0]))
            csvtable.append(temp)
            # writing result to csv
            write.writerow(csvtable)
            temp.clear()
            csvtable.clear()

    f.close()


    # storing different(by experiment value) tf_idf result to csv
    temp = []
    for i in value:
        fileName = str(i)
        f = open(_resultDir + fileName+'.csv', 'w', newline='')
        write = csv.writer(f)
        for r in range(len(result)):
            if result[r][1] > i:
                temp.append(HanziConv.toTraditional(result[r][0]))
                temp.append(result[r][1])
                write.writerow(temp)
            temp.clear()
        f.close()



# ====== initial setting ======

# jieba setting
print("Start loading initial setting!")
relativePath = os.getcwd()
jieba.analyse.set_stop_words(relativePath + "/jieba_setting/stopwords.txt")

# ====== initial setting ======

if __name__ == "__main__":
    main()