########################################################################################################################
####                                                KMeans Clustering
########################################################################################################################

import pickle
from scipy import sparse
from sklearn.cluster import KMeans
from scipy.sparse import hstack

N_grams = (1,2)

MyFeatures = []
for j in N_grams:
    MyFeatures.append(sparse.load_npz('MyFeatures_'.__add__(str(j).__add__('_gram.npz'))))
MyFeatures = hstack(tuple(MyFeatures[0:N_grams.__len__()]))

my_clusters = range(2,22,1)

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
tipo = tipo.replace(',','')
with open('MyCentroid_'.__add__(tipo).__add__('.csv'), "wb") as file:
    pickle.dump(Centroid, file)
with open('MyLabels_'.__add__(tipo).__add__('.csv'), "wb") as file:
    pickle.dump(Cluster_labels, file)
with open('MyInertia_'.__add__(tipo).__add__('.csv'), "wb") as file:
    pickle.dump(Inertia, file)
with open('ClusterFreq_'.__add__(tipo).__add__('.csv'), "wb") as file:
    pickle.dump(ClusterFreq, file)