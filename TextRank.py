# -*- coding: UTF-8 -*-
import jieba
from jieba import analyse
import os

def textrank(corpus):

    print("Start process Textrank!")
    textrank = jieba.analyse.textrank(corpus, withWeight=True, topK=200)

    return textrank

