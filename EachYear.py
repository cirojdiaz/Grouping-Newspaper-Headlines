########################################################################################################################
####                                                KMeans Clustering
########################################################################################################################

import pickle
import numpy as np
from scipy import sparse
from sklearn.cluster import KMeans
from scipy.sparse import hstack
N_grams = (1,2)
MyFeatures = []
for j in N_grams:
    MyFeatures.append(sparse.load_npz('MyFeatures_'.__add__(str(j).__add__('_gram.npz'))))
MyFeatures = hstack(tuple(MyFeatures[0:N_grams.__len__()]))
MyFeatures = MyFeatures.tocsr()
my_years = int(1000001/15)*np.array(range(16))
K_optim = 19

Cluster_labels=[]
Inertia = []
ClusterFreq = []
Centroid = []

for n in range(15):
    ThisFeature = MyFeatures[my_years[n]:my_years[n+1]]
    kmeans = KMeans(n_clusters=K_optim, init='k-means++', n_init=10+K_optim, max_iter=100, tol=0.01,\
                     precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1, algorithm='auto')

    MyLabel = kmeans.fit_predict(ThisFeature)
    MyCentroid = kmeans.cluster_centers_
    MyInertia = kmeans.inertia_

    Centroid.append(MyCentroid)
    Cluster_labels.append(MyLabel)
    Inertia.append(MyInertia)

    Freq = [0] * K_optim
    for i in MyLabel:
        Freq[i-1] += 1
    print(Freq)
    ClusterFreq.append(Freq)

tipo = str(N_grams).replace(', ','')

with open('MyCentroid_'.__add__(tipo).__add__('(years).csv'), "wb") as file:
    pickle.dump(Centroid, file)
with open('MyLabels_'.__add__(tipo).__add__('(years).csv'), "wb") as file:
    pickle.dump(Cluster_labels, file)
with open('MyInertia_'.__add__(tipo).__add__('(years).csv'), "wb") as file:
    pickle.dump(Inertia, file)
with open('ClusterFreq_'.__add__(tipo).__add__('(years).csv'), "wb") as file:
    pickle.dump(ClusterFreq, file)