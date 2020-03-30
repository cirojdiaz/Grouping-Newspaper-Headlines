import pickle
import numpy as np
N_grams = (1,2)

tipo = str(N_grams).replace(', ','')
with open('MyLabels_'.__add__(tipo).__add__('(years).csv'), "rb") as file:
    MyLabels= pickle.load(file)
with open('MyInertia_'.__add__(tipo).__add__('(years).csv'), "rb") as file:
    MyInertia = pickle.load(file)
with open('ClusterFreq_'.__add__(tipo).__add__('(years).csv'), "rb") as file:
    MyCluster = pickle.load(file)


with open('MyLabels_'.__add__(tipo).__add__('_matlab(years).txt'),'w') as file:
    file.write(str(MyLabels))
with open('MyInertia_'.__add__(tipo).__add__('_matlab(years).txt'),'w') as file:
    file.write(str(MyInertia))
with open('ClusterFreq_'.__add__(tipo).__add__('_matlab(years).txt'),'w') as file:
    file.write(str(MyCluster))

# tipo = str(N_grams).replace(', ','')
# with open('MyLabels_'.__add__(tipo).__add__('.csv'), "rb") as file:
#     MyLabels= pickle.load(file)
# with open('MyInertia_'.__add__(tipo).__add__('.csv'), "rb") as file:
#     MyInertia = pickle.load(file)
# with open('ClusterFreq_'.__add__(tipo).__add__('.csv'), "rb") as file:
#     MyCluster = pickle.load(file)
#
# tipo = tipo.replace(',','')
#
# with open('MyLabels_'.__add__(tipo).__add__('_matlab.txt'),'w') as file:
#     file.write(str(MyLabels))
# with open('MyInertia_'.__add__(tipo).__add__('_matlab.txt'),'w') as file:
#     file.write(str(MyInertia))
# with open('ClusterFreq_'.__add__(tipo).__add__('_matlab.txt'),'w') as file:
#     file.write(str(MyCluster))
