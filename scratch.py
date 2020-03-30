import re, nltk
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
MyDict={}
with open('news_headlines.csv') as data:
    # i=0
    # c=0
    for line in data:
        # c+=1
        # print(c)
        line=line.replace(';;;;;','')
        line=line.replace('\n','')
        values=line.split(sep=',')
        val=values[1].split(sep=' ')
        for word in val:
            if re.match("^[a-z_]*$", word) and len(word)>2:
                tags = nltk.pos_tag([word])   # preparing format to keep nouns only
                if tags[0][1] == 'NN':        # Keeping nouns only
                    word = stemmer.stem(word) # Taking root of the word
                    if not(word in MyDict):
                        MyDict[word] = 1
                    else:
                        MyDict[word]+=1
MyList = []
MyFrequencies =[]
for key in MyDict:
    MyList.append(key)
    MyFrequencies.append(MyDict[key])


with open("MyList.txt", "w") as file:
    file.write(str(MyList))
with open("MyFrequencies.txt", "w") as file:
    file.write(str(MyFrequencies))



import numpy, time, scipy
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
with open("MyList.txt", "r") as file:
    my_list = eval(file.readline())
with open("MyFrequencies.txt", "r") as file:
    my_frquencies = eval(file.readline())

my_frequencies = numpy.array(my_frquencies)
my_list = numpy.array(my_list)
sort_index = numpy.argsort(my_frquencies)[::-1]
my_list = my_list[sort_index][:300]
my_frequencies = my_frequencies[sort_index][:300]
my_list = my_list.tolist()
my_frequencies = my_frequencies.tolist()

with open('news_headlines.csv') as data:
    i = 0
    for line in data:
        print(i)
        Feat = [0]*300
        line = line.replace(';;;;;', '')
        line=line.replace('\n','')
        values = line.split(sep=',')
        values = stemmer.stem(values[1])  # Taking root of the word:
        values = values.split(sep=' ')
        for word in my_list:
            if word in values:
                ind = my_list.index(word)
                Feat[ind]=1
                Feat = [int(i) for i in Feat]
        b = scipy.sparse.csr_matrix(Feat)
        if i==0:
            Features = scipy.sparse.csr_matrix(Feat)
        else:
            Features.data = numpy.hstack((Features.data, b.data))
            Features.indices = numpy.hstack((Features.indices, b.indices))
            Features.indptr = numpy.hstack((Features.indptr, (b.indptr + Features.nnz)[1:]))
            Features._shape = (Features.shape[0] + b.shape[0], b.shape[1])
        i+=1

scipy.sparse.save_npz('MyFeatures.npz', Features)

from scipy import sparse
MyFeatures = sparse.load_npz('MyFeatures.npz')























