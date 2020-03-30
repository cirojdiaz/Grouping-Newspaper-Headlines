import pickle, numpy
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
MyDict={}
N_grams = 1
with open('WORKED_news_headlines_FeatONE.csv','rb') as file:
    data = pickle.load(file)
i=0
for line in data:
    print(i)
    line = word_tokenize(line)
    for j in range(line.__len__()-(N_grams-1)):
        MyGram = tuple(line[j:j+N_grams])
        if not(MyGram in MyDict):
            MyDict[MyGram] = 1
        else:
            MyDict[MyGram]+=1
    i += 1
MyList = []
MyFrequencies =[]
for key in MyDict:
    MyList.append(key)
    MyFrequencies.append(MyDict[key])

sort_index = numpy.argsort(MyFrequencies)
sort_index = sort_index[::-1]
MyFrequencies = [MyFrequencies[i] for i in sort_index]
MyList = [MyList[i] for i in sort_index]

with open('MyList_'.__add__(str(N_grams).__add__('_gram.txt')), "w") as file:
    file.write(str(MyList))
with open('MyFrequencies_'.__add__(str(N_grams).__add__('_gram.txt')), "w") as file:
    file.write(str(MyFrequencies))