
import requests
import jieba
import time
import os
from TextRank import textrank
from TextRankRes import textrankRes
from TextRankJob import textrankJob

def nowtime():
    return time.time()

def main():
    sTime = nowtime()
    
    # scrawler setting
    print("Start get scrawler data!")
    url = "http://140.124.183.5:8983/solr/EBCStation/select?indent=on&q=*:*&rows=500&wt=json"
    article = requests.get(url).json()
    
    print("Scrawler took %.fs." % (time.time()-sTime))
    # db length
    name = ['兒童新聞', '創設市集', '技職最前線', '教育開講', '星期講座', '不太乖學堂','國際教育心動線']
    articleLen = article['response']['numFound']
    for n in name:
        corpus = ""
        sTime = nowtime()
        for a in range(articleLen):
            try:
                temp = article['response']['docs'][a]['name']
            except KeyError:
                continue
            if article['response']['docs'][a]['name'] == n:
                corpus += article['response']['docs'][a]['content']
        # call textrank function
        sTime = nowtime()
        #trRes = textrank(corpus)
        #print("Name: %s textrank calculate took %.fs." % ((n),(time.time()-sTime)))

        # call store textrank result function
        sTime = nowtime()
        #textrankRes(n,trRes)
        #print("Store %s textrank result took %.fs." % ((n),(time.time()-sTime)))
        
        # call experiment function
        sTime = nowtime()
        textrankJob(n)
        print("Name: %s textrank match took %.fs." % ((n),(time.time()-sTime)))

 # jieba setting
print("Start loading initial setting!")
relativePath = os.getcwd()
jieba.analyse.set_stop_words(relativePath + "/jieba_setting/stopwords.txt")

if __name__ == "__main__":
    main()