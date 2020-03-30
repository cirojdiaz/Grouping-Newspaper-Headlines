############################################################################################
#                           Ingenheiring my Data  2-gram                                   #
############################################################################################
import numpy, pickle, operator
from scipy import sparse
from nltk import word_tokenize

for N_grams in range(1,2+1,1):

    with open('MyList_'.__add__(str(N_grams).__add__('_gram.txt')), "r") as file:
        my_list = eval(file.readline())
    with open('MyFrequencies_'.__add__(str(N_grams).__add__('_gram.txt')), "r") as file:
        my_frequencies = eval(file.readline())

    Cut = 1
    Threshold = Cut*(20*(N_grams==1) + 2*(N_grams==2) + 7*(N_grams==3) +3*(N_grams==4))
    # ThrsUP = numpy.mean(my_frequencies)

    my_frequencies = numpy.array(my_frequencies)
    Thr_index = numpy.array(numpy.argwhere(my_frequencies >= Threshold))
    Thr_index = Thr_index.flatten()
    n_features = Thr_index.__len__()
    my_list = operator.itemgetter(*Thr_index)(my_list)
    my_frequencies = operator.itemgetter(*Thr_index)(my_frequencies)
    my_dict = dict(zip(my_list,range(n_features)))

    with open('WORKED_news_headlines.csv','br') as file:
        data = pickle.load(file)
    i = 0
    FeatX = []
    FeatY = []
    FeatV = []
    for line in data:
        print((N_grams,i))
        line = word_tokenize(line)
        line_N_grams = range(line.__len__() - (N_grams - 1))
        for j in line_N_grams:
            MyGram = tuple(line[j:j + N_grams])
            try:
                FeatY.append(my_dict[MyGram])
                FeatX.append(i)
                FeatV.append(1)
            except KeyError:
                pass
        i += 1
    DIM = [i,n_features]
    numpy.savetxt('FeatX.txt_'.__add__(str(N_grams).__add__('_gram.txt')),FeatX,delimiter=',',fmt='%i')
    numpy.savetxt('FeatY.txt_'.__add__(str(N_grams).__add__('_gram.txt')),FeatY,delimiter=',',fmt='%i')
    numpy.savetxt('FeatV.txt_'.__add__(str(N_grams).__add__('_gram.txt')),FeatV,delimiter=',',fmt='%i')
    numpy.savetxt('DIM.txt_'.__add__(str(N_grams).__add__('_gram.txt'))  ,DIM  ,delimiter=',',fmt='%i')
    SpFeatures = sparse.coo_matrix((FeatV,(FeatX,FeatY)),(DIM[0],DIM[1]))
    sparse.save_npz('MyFeatures_'.__add__(str(N_grams).__add__('_gram.npz')), SpFeatures)

    with open('MyDictList_'.__add__(str(N_grams).__add__('_gram.txt')), "w") as file:
        file.write(str(my_list))