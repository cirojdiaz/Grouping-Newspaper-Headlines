import re, pickle
from nltk import pos_tag, word_tokenize
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
MyData=[]
i = 0
with open('news_headlines.csv') as data:
    for line in data:
        print(i)
        line=line.replace(';','')
        line=line.replace('\n','')
        values=line.split(sep=',')
        values = word_tokenize(values[1])
        val = []
        for word in values:
            if re.match("^[a-z_]*$", word):
                tags = pos_tag([word])   # preparing format to keep nouns only
                if tags[0][1] in ('NN','NNP','JJ','NNS','RB','VB','VBD','VBG','VBN','VBP','VBZ') and len(word)>=2:       # Keeping the verbs, sustantives, verbs and adverbs
                    val.append(stemmer.stem(word))
        MyData.append(str(' '.join(val)))
        i+=1

with open('WORKED_news_headlines.csv', "wb") as file:
    pickle.dump(MyData, file)

