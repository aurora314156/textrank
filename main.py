
import requests
import jieba
import time
import os
from TextRank import textrank
from TextRankRes import textrankRes

def main():
    sTime = time.time()
    
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
        sTime = time.time()
        for a in range(articleLen):
            try:
                temp = article['response']['docs'][a]['name']
            except KeyError:
                continue
            if article['response']['docs'][a]['name'] == n:
                corpus += article['response']['docs'][a]['content']
        # call textrank function
        trRes = textrank(corpus)
        print("Name: %s textrank took %.fs." % ((n),(time.time()-sTime)))
        
        # call store result function
        textrankRes(n, trRes)


 # jieba setting
print("Start loading initial setting!")
relativePath = os.getcwd()
jieba.analyse.set_stop_words(relativePath + "/jieba_setting/stopwords.txt")

if __name__ == "__main__":
    main()