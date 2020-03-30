########################################################################################################################
####                                                KMeans Clustering
########################################################################################################################

import pickle
import numpy as np
from scipy import sparse
from sklearn.cluster import KMeans
from scipy.sparse import hstack
N_grams = (1,2,3,4)
MyFeatures = []
for j in N_grams:
    MyFeatures.append(sparse.load_npz('MyFeatures_'.__add__(str(j).__add__('_gram.npz'))))
MyFeatures = hstack(tuple(MyFeatures[0:N_grams.__len__()]))
my_clusters = range(10,150,10)

Cluster_labels=[]
Inertia = []
ClusterFreq = []
Centroid = []

for n in my_clusters:
    kmeans = KMeans(n_clusters=n, init='k-means++', n_init=10, max_iter=100, tol= .01,\
                     precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1, algorithm='auto')

    MyLabel = kmeans.fit_predict(MyFeatures)
    MyCentroid = kmeans.cluster_centers_
    MyInertia = kmeans.inertia_

    Centroid.append(MyCentroid)
    Cluster_labels.append(MyLabel)
    Inertia.append(MyInertia)

    Freq = [0] * n
    for i in MyLabel:
        Freq[i-1] += 1
    print(Freq)
    ClusterFreq.append(Freq)

tipo = str(N_grams).replace(', ','')
with open('MyCentroid_'.__add__(tipo).__add__('.csv'), "wb") as file:
    pickle.dump(Centroid, file)
with open('MyLabels_'.__add__(tipo).__add__('.csv'), "wb") as file:
    pickle.dump(Cluster_labels, file)
with open('MyInertia_'.__add__(tipo).__add__('.csv'), "wb") as file:
    pickle.dump(Inertia, file)
with open('ClusterFreq_'.__add__(tipo).__add__('.csv'), "wb") as file:
    pickle.dump(ClusterFreq, file)


# Center = np.nonzero(MyCentroid[0])
# print(Center)
#
# with open('MyDictList_'.__add__(str(1).__add__('_gram.txt')), "r") as file:
#     list1 = eval(file.readline())
# with open('MyDictList_'.__add__(str(2).__add__('_gram.txt')), "r") as file:
#     list2 = eval(file.readline())
# LISTA = list1+list2
#
# for j in range(20):
#     for i in Center[j]:
#         print(LISTA[i])
#         print('*************************************************************')
