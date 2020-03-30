import pickle

with open('MyLabels_1.csv', "rb") as file:
    MyLabels_1= pickle.load(file)

with open('news_headlines.csv') as data:
    c = 0
    for line in data:
        line=line.replace(';','')
        line=line.replace('\n','')
        values=line.split(sep=',')
        values = values[1]
        Label = MyLabels_1[0]
        if Label[c]==0:
            print(values)
        c +=1
