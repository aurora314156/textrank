import jieba.posseg as pseg
from hanziconv import HanziConv

# 標註所有名詞詞性的詞
def posTagging(word, n):
    try:
        # tfidf result was simplified words.
        if n != 'tfidf':
            simpWord = HanziConv.toSimplified(word)
        else:
            simpWord = word
        tagRes = pseg.cut(simpWord)
    except ValueError:
        return 0
    for word, tag in tagRes:
        if 'n' in tag:
            return 1
    return 0
     