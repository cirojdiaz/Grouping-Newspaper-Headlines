import pickle
import numpy as np
from wordcloud import WordCloud, STOPWORDS


import wikipedia

N_grams = (1,2)
#
# with open('news_headlines.csv') as data:
#     MyData = []
#     i = 0
#     for line in data:
#         print(i)
#         line=line.replace(';','')
#         line=line.replace('\n','')
#         line = line.replace("'s", '')
#         line = line.replace("'", '')
#         line = line.split(sep=',')[1]
#         MyData.append(line)
#         i+=1
#
# with open('news_headlines_CLEAN.csv', "wb") as file:
#     pickle.dump(MyData, file)

with open('news_headlines_CLEAN.csv','rb') as file:
    MyData = pickle.load(file)

tipo = str(N_grams).replace(', ','')
with open('MyLabels_'.__add__(tipo).__add__('.csv'), "rb") as file:
    MyLabels = pickle.load(file)

with open('MyCentroid_'.__add__(tipo).__add__('.csv'), "rb") as file:
    MyCentroid = pickle.load(file)

NN = 18
for j in range(0,NN):
    C0 = MyCentroid[NN][j]
    NonZero = np.argwhere(C0>0).tolist()
    nel = len(NonZero)
    print(NonZero)

i = 0
for label in MyLabels:
    print(i)
    index = np.argwhere(np.array(label)==i).tolist()
    Text = str(np.array(MyData)[index].tolist())
    stopword = set(STOPWORDS)
    my_cloud = WordCloud(background_color='white', max_words=100, stopwords=stopword)
    my_cloud.generate(Text)
    my_cloud.to_file('wcloud'.__add__(str(i)).__add__('.png'))
    i+=1

